Dynamic Batching

Dynamic batching is a feature of Inferless that allows inference requests to be combined by the server so that a batch is created dynamically. Creating a batch of requests typically results in increased throughput. The dynamic batcher should be used for the stateless model. 
Dynamic batching is enabled and configured independently for each model using the BATCH_SIZE property in the model configuration. These settings control the preferred batch size(s) of the dynamically created batches, the maximum time that requests can be delayed in the scheduler to allow other requests to join the dynamic batch, and queue properties such as batch_window
