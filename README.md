# Grass cutter

## Usage

### Traning

![Video Training](./movies/train.gif)

```
python main.py
```

### Run the trained model

![Video Run](./movies/main.gif)

```
python main.py <number of episodes>
```
eq.

```
python main.py 1200
```

Pygame version

![Video Run Pygame](./movies/gui.gif)

```
python gui.py <number of episodes>
```

eq.

```
python gui.py 1200
```

## Configuration

Confuguration is in `config.py`

*LAWN_SIZE*: Size of the lawn

*EPISODES*: Number of episodes

*PICKLE_STEP*: Save the model every PICKLE_STEP episodes

*EPSILON*: Epsilon for epsilon-greedy

*ALPHA*: Learning rate

*GAMMA*: Discount factor