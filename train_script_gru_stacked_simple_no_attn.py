from models import gru_stacked_simple
from helpers import checkpoint

# Get the review summary file
review_summary_file = 'extracted_data/review_summary.csv'

# Initialize Checkpointer to ensure checkpointing
checkpointer = checkpoint.Checkpointer('stackedSimple','gru','noAttention')
checkpointer.steps_per_checkpoint(1000)
checkpointer.steps_per_prediction(2000)
# Do using GRU cell - without attention mechanism
out_file = 'result/stacked_simple/gru/no_attention.csv'
checkpointer.set_result_location(out_file)
gru_net = gru_stacked_simple.NeuralNet(review_summary_file, checkpointer)
gru_net.set_parameters(train_batch_size=10,test_batch_size=10, memory_dim=7,learning_rate=0.008)
gru_net.begin_session()
gru_net.form_model_graph(num_layers=2)
gru_net.fit()
gru_net.predict()
gru_net.store_test_predictions()
gru_net.close_session()
