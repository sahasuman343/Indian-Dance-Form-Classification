#Creating Model
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.vgg16 import VGG16



vgg = VGG16(include_top = False,
                            input_shape = (156,156,3),
                            weights = 'imagenet')

print(vgg.summary())

vgg.trainable = True
print(len(vgg.layers))

fine_tune_at = 17

for layer in vgg.layers[:fine_tune_at]:
    layer.trainable = False

last_output = vgg.output

x = tf.keras.layers.Flatten()(last_output)
x = tf.keras.layers.Dense(1024, activation = 'relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(8, activation = 'softmax')(x)


model = tf.keras.Model(vgg.input, x)

print(model.summary())

model.compile(tf.keras.optimizers.RMSprop(lr = 0.001), loss='categorical_crossentropy', metrics=['acc'])

cb1= tf.keras.callbacks.ReduceLROnPlateau(monitor='val_acc', 
                                            patience=3, 
                                            verbose=1, 
                                            factor=0.5, 
                                            min_lr=0.00001)
cb2=tf.keras.callbacks.ModelCheckpoint("best_model.h5",save_best_only=True)


#generate image
train_path= r'data/train'
valid_path= r'data/valid'
train_datagen = ImageDataGenerator(rescale=1./255,
                                  rotation_range=20,
                                  width_shift_range=0.2,
                                  height_shift_range=0.2,
                                  shear_range=0.1,
                                  zoom_range=0.2,
                                  horizontal_flip=True,
                                  fill_mode='nearest')

validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(train_path,
                                                   target_size=(156,156),
                                                   color_mode = 'rgb',
                                                   batch_size=32,
                                                   class_mode='categorical')


valid_generator = validation_datagen.flow_from_directory(valid_path,
                                                   target_size=(156,156),
                                                   color_mode = 'rgb',
                                                   batch_size=32,
                                                   class_mode='categorical')


history = model.fit_generator(train_generator,
                              epochs=40,
                              verbose=1,
                              validation_data=valid_generator,
                              callbacks = [cb1,cb2])

