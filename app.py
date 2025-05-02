import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"]='1'
from huggingface_hub import snapshot_download
from transformers import AutoProcessor, AutoModelForImageTextToText
import torch
import requests
import tempfile

class InferlessPythonModel:
    def initialize(self):
        model_path = "HuggingFaceTB/SmolVLM2-2.2B-Instruct"
        
        # Download the model
        snapshot_download(repo_id=model_path, allow_patterns=["*.safetensors"])
        
        # Initialize processor and model
        self.processor = AutoProcessor.from_pretrained(model_path)
        self.model = AutoModelForImageTextToText.from_pretrained(
            model_path,
            torch_dtype=torch.bfloat16,
            _attn_implementation="flash_attention_2"
        ).to("cuda")
    

    def download_video(self, url):
        """Download video from URL to a temporary file"""
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
                for chunk in response.iter_content(chunk_size=8192):
                    temp_file.write(chunk)
                return temp_file.name
        else:
            raise Exception(f"Failed to download video: {response.status_code}")
    
    def infer(self, inputs):
        output = []
        print("No of inputs to be processed " + str(len(inputs)))
        
        for each in inputs:
            prompt = each.get("text", "Describe the video" )
            video_url = each.get("video_url", "https://file-examples.com/wp-content/storage/2017/04/file_example_MP4_640_3MG.mp4")
            
            try:
                # Download the video if it's a URL
                if video_url.startswith(('http://', 'https://')):
                    video_path = self.download_video(video_url)
                else:
                    video_path = video_url
                
                # Create the messages with video content
                messages = [
                    {
                        "role": "user",
                        "content": [
                            {"type": "video", "path": video_path},
                            {"type": "text", "text": prompt}
                        ]
                    },
                ]
                
                # Apply chat template and tokenize
                inputs_tensor = self.processor.apply_chat_template(
                    messages,
                    add_generation_prompt=True,
                    tokenize=True,
                    return_dict=True,
                    return_tensors="pt",
                ).to(self.model.device, dtype=torch.bfloat16)
                
                # Generate response
                generated_ids = self.model.generate(**inputs_tensor, do_sample=False, max_new_tokens=500)
                
                # Decode the response
                generated_texts = self.processor.batch_decode(
                    generated_ids,
                    skip_special_tokens=True,
                )
                
                generated_text = generated_texts[0] if generated_texts else ""
                
                print("generated_text", generated_text, flush=True)
                output.append({"generated_text": generated_text})
                
                # Clean up temporary file if it was downloaded
                if video_url.startswith(('http://', 'https://')):
                    os.unlink(video_path)
                    
            except Exception as e:
                output.append({"error": "Could not process input"})
        
        return output
    
    def finalize(self, args):
        self.processor = None
        self.model = None
