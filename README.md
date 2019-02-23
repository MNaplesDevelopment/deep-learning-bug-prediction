# machine-learning-bug-prediction

This is a very simple 3 layered nerual network written from scratch, most of the code was from assignments I worked on at https://deeplearning.ai I did however add L2 cost regularization which helps the model descend down the loss function and reach the global minimum without getting caught up in some of the ripples of the error plane by smoothing the plane out and making it more convex.

I regrettably lost my source for this data but the data contains information describing the overall complexity of a programming project. It contains information like the number of lines of code, depth of inheritance, number of variables, etc. This model can predict with about 93% accuracy if there is atleast 1 bug in the software.

Chech out [my other](https://github.com/MNaplesDevelopment/deep-learning-software-defects) deep learning project which is much more complicated and takes a natural language processing approach to bug detection.

# Tuning hyperparameters:

To alter the number of neurons in the hidden layer, change n_h on lines 47 and 63, and change the parameter on line 243 to match.

The number of iterations can also be changed on 243.

The learning rate can be changed on line 214.
