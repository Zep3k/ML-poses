import numpy as np
import sys

class LinearRegression(object):
    """
        Linear regressor object. 
        Note: This class will implement BOTH linear regression and ridge regression.
        Recall that linear regression is just ridge regression with lambda=0.
        Feel free to add more functions to this class if you need.
        But make sure that __init__, set_arguments, fit and predict work correctly.
    """

    def __init__(self, *args, **kwargs):
        """
            Initialize the task_kind (see dummy_methods.py)
            and call set_arguments function of this class.
        """
        self.task_kind = 'regression'
        self.iters = 1000
        self.set_arguments(*args, **kwargs)

    def set_arguments(self, *args, **kwargs):
        """
            args and kwargs are super easy to use! See dummy_methods.py
            In case of ridge regression, you need to define lambda regularizer(lmda).

            You can either pass these as args or kwargs.
        """

        if "lambda" in kwargs:
            self.reg_arg = kwargs["lambda"]
        # if not, then check if args is a list with size bigger than 0.
        elif len(args) > 0 :
            self.reg_arg = args[0]
        # if there were no args or kwargs passed, we set the dummy_arg to 1 (default value).
        else:
            self.reg_arg = 1
    

    def fit(self, training_data, training_labels):
        """
            Trains the model, returns predicted labels for training data.
            Arguments:
                training_data (np.array): training data of shape (N,D)
                training_labels (np.array): regression target of shape (N,regression_target_size)
            Returns:
                pred_regression_targets (np.array): predicted target of shape (N,regression_target_size)
        """
        self.D = training_data.shape[1] 
        self.N = training_data.shape[0]
        self.regression_target_size = training_labels.shape[1]
        training_data1 = np.insert(training_data, 0, 1, axis=1)
        print(training_data1)
        pred_regression_target = np.linalg.pinv(training_data1)@(training_labels)
        
        self.w = pred_regression_target
        pred_regression_targets= training_data1 @ self.w
        return pred_regression_targets
    def predict(self, test_data):
        """
            Runs prediction on the test data.
            
            Arguments:
                test_data (np.array): test data of shape (N,D)
            Returns:
                pred_regression_targets (np.array): predicted targets of shape (N,regression_target_size)
        """
        test_data = np.insert(test_data, 0, 1, axis=1)
        print(test_data)
        pred_regression_targets = np.dot(test_data, self.w)
        return pred_regression_targets

