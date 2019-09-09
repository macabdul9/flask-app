from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from keras.utils.np_utils import to_categorical
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.layers import *
from keras.optimizers import *



class Model:

	def creat_n_compile():
		model = Sequential()
		model.add(Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=X.shape[1]))
		#model.add(SpatialDropout1D(0.2))
		model.add(LSTM(64))
		model.add(Dense(11, activation='softmax'))
		model.compile(loss='categorical_crossentropy', optimizer=radam, metrics=['accuracy'])

		return model
