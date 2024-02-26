
# Tutorial - Dynamic Batching with GPT Neo using Inferless

Check out which will guide you through the process of deploying a GPT neo model using Inferless.

Dynamic batching is a feature of Inferless that allows inference requests to be combined by the server so that a batch is created dynamically. Creating a batch of requests typically results in increased throughput. The dynamic batcher should be used for the stateless model. 
Dynamic batching is enabled and configured independently for each model using the BATCH_SIZE property in the model configuration. These settings control the preferred batch size(s) of the dynamically created batches, the maximum time that requests can be delayed in the scheduler to allow other requests to join the dynamic batch, and queue properties such as batch_window

---
## Prerequisites
- **Git**. You would need git installed on your system if you wish to customize the repo after forking.
- **Python>=3.8**. You would need Python to customize the code in the app.py according to your needs.
- **Curl**. You would need Curl if you want to make API calls from the terminal itself.

---
## Quick Tutorial on "How to Deploy" on Inferless
Here is a quick start to help you get up and running with this template on Inferless.

### Download the config and Create a runtime 
Get started by downloading the config.yaml file and go to Inferless dashboard and create a custom runtime.

Quickly add this as a Custom runtime.

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.


### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the Add Model button.

Select the PyTorch as framework and choose **Repo(custom code)** as your model source and use the forked repo URL as the **Model URL**.

After the create model step, while setting the configuration for the model make sure to select the appropriate runtime.

Enter all the required details to Import your model. Refer [this link](https://docs.inferless.com/integrations/github-custom-code) for more information on model import.

The following is a sample Input and Output JSON for this model which you can use while importing this model on Inferless.


---
## Curl Command
Following is an example of the curl command you can use to make inferences. You can find the exact curl command on the Model's API page in Inferless. First Dimension is batch Size 


```bash
curl --location 'https://m-f1b125b27c98484bbf5dae6d018f7b99-m.default.model-v1.inferless.com/v2/models/example-batch_f1b125b27c98484bbf5dae6d018f7b99/versions/1/infer' \
          --header 'Content-Type: application/json' \
          --header 'Authorization: Bearer 76e617c43537f68af57922d36cbfbf0236775a6b37f4f8a04ab5ed0b132dcc6d81984b9ce1153e4be81b595e21f49c08d0eda760d22ef1ebb3b24af7ccd39b56' \
          --data '{
    "inputs": [
        {
            "name": "prompt",
            "shape": [
                1,
                1
            ],
            "data": [
                "There is a fine house in the forest"
            ],
            "datatype": "BYTES"
        }
    ]
}'
```


---
## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer, and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in the inputs. Refer to [input](#input) for more.

```python
def infer(self, inputs):
    prompt = inputs["prompt"]
```

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the GPU by setting `self.pipe = None`.


For more information refer to the [Inferless docs](https://docs.inferless.com/).
