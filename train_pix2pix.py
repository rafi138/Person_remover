import tensorflow as tf
from absl import flags, app
from absl.flags import FLAGS
from pix2pix.utils.model import Pix2Pix
from pix2pix.utils.dataset import train_pipeline, test_pipeline

flags.DEFINE_integer('buffer_size', 100, 'size of buffer')
flags.DEFINE_integer('width', 256, 'width of resulting images')
flags.DEFINE_integer('height', 256, 'height of resulting images')
flags.DEFINE_float('lambda_p', 100, 'lambda parameter')
flags.DEFINE_integer('epochs', 100, 'Number of epochs to train from', short_name='e')
flags.DEFINE_string('checkpoint', 'pix2pix/checkpoint/', 'Checkpoint directory')
flags.DEFINE_string('training_dir', 'input/training/images/', 'Path for training samples', short_name='train')
flags.DEFINE_string('testing_dir', 'input/testing/images/', 'Path for testing samples', short_name='test')
flags.DEFINE_bool('restore_check', False, 'Restore last checkpoint in folder --checkpoint', short_name='restore')

# BUFFER_SIZE = 100
# BATCH_SIZE = 1
# IMG_WIDTH = 416
# IMG_HEIGHT = 416
# LAMBDA = 10
# EPOCHS = 100
# PATH_training = '../input/training/prueba/'
# PATH_testing = '../input/testing/prueba/'
# checkpoint_dir = '../pix2pix/checkpoint/'

def main(_argv):
    train_dataset = train_pipeline(FLAGS.training_dir, FLAGS.buffer_size, FLAGS.width, FLAGS.height)
    test_dataset = test_pipeline(FLAGS.testing_dir, FLAGS.width, FLAGS.height)

    p2p = Pix2Pix(train_dataset, test_dataset, FLAGS.lambda_p, FLAGS.epochs, FLAGS.checkpoint, FLAGS.restore_check)
    p2p.fit()

if __name__ == '__main__':
    try:
        app.run(main)
    except Exception as e:
        print(f'Error: {e}')
