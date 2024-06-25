import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Генерация данных
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Создание модели
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))  # Входной слой + 1 скрытый слой с 4 нейронами
model.add(Dense(1, activation='sigmoid'))  # Выходной слой

# Компиляция модели
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Тренировка модели
model.fit(X, y, epochs=1000, verbose=0)

# Вывод структуры модели
model.summary()