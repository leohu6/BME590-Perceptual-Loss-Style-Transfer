import time
import argparse

def get_config():
    parser = argparse.ArgumentParser()

    # Input parser
    parser.add_argument('--bs',       default=4,    type=int, help='batch size')
    parser.add_argument('--in_h',     default=256,  type=int, help='image input size height')
    parser.add_argument('--in_w',     default=256,  type=int, help='image input size width')
    parser.add_argument('--epochs',   default=50,  type=int, help='number of epochs')
    parser.add_argument('--m',        default=True, type=bool, help='manual run or hp tuning')
    parser.add_argument('--is_test',  default=False, type=bool, help='is test')

#     parser.add_argument('--train_csv', default='gs://duke-research-us/mimicknet/data/training-v2.csv', help='csv for paired training')
#     parser.add_argument('--validation_csv', default='gs://duke-research-us/mimicknet/data/validation-v2.csv', help='csv for validation')
#     parser.add_argument('--test_csv', default='gs://duke-research-us/mimicknet/data/testing-v2.csv', help='csv for testing')
    
#     # Cloud ML Params
#     parser.add_argument('--job-dir', default='gs://duke-research-us/mimicknet/tmp/{}'.format(str(time.time())), help='Job directory for Google Cloud ML')
#     parser.add_argument('--model_dir', default='./trained_models', help='Directory for trained models')
#     parser.add_argument('--image_dir', default='gs://duke-research-us/mimicknet/data/duke-ultrasound-v1', help='Local image directory')
    
    parsed, unknown = parser.parse_known_args()
    
    print('Unknown args:', unknown)
    print('Parsed args:', parsed.__dict__)
    
    return parsed

config = get_config()