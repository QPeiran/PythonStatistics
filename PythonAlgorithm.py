import pandas as pd
import datetime as dt
import numpy as np
from math import *
import time
#data = pd.read_excel (r'C:\Users\Peiran Quan\Desktop\W51.xlsx') 
#print(data)
"""
df = pd.DataFrame(data, columns=['Barcode', 'Timestamp','Date','Team Leader'])

## read columns
print (df[['Barcode','Timestamp']]) # for extracting more than 1 columns , double [] is required

## read headers
print(df.columns)

## read rows
print(df.iloc[0:5])

## read [row,column]
print(df.iloc[5,3])

counter = 0

for A,B in df.iterrows():
    print(A,B['Barcode'])
    counter += 1
    if counter >= 10:
        break

## filter by "Break Start"
BSFrame = df.loc[df['Barcode'] == 'Break Start']
#print(BSFrame)
## Summary
#print(BSFrame.describe())
## Sorting -- Both 'Date' & 'Timestamps" are descending
BSFrame_sorted = BSFrame.sort_values(['Date','Timestamp'], ascending = [False,False])
print(BSFrame_sorted)
"""

"""
def categorize_event_shift(timestamp):
    weekday_index = pd.Timestamp(timestamp).weekday()
    switcher = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    weekday = switcher.get(weekday_index,'')
    hour = pd.Timestamp(timestamp).hour
    if hour in range(6,13):
        shift = 'Morning Shift'
    elif hour in range(14,22):
        shift = 'Afternoon Shift'
    else:
        shift = 'Error'
    return weekday +' '+ shift

"""

#staged_df = pd.read_csv(r'C:\Users\Peiran Quan\Desktop\W51staged.csv')
"""
print(staged_df["Timestamp and Date"][1])
print(staged_df["Timestamp and Date"][2])

t1 = pd.to_datetime(staged_df["Timestamp and Date"][1])
t2 = pd.to_datetime(staged_df["Timestamp and Date"][2])
weekday = pd.Timestamp(staged_df["Timestamp and Date"][1]).weekday()
hour = pd.Timestamp(staged_df["Timestamp and Date"][1]).hour
weekday_shift = categorize_event_shift(staged_df["Timestamp and Date"][2])
InMin = pd.Timedelta(t2-t1).seconds/60.0

def count_pickers(picker):
    picker_array = picker.split(';')
    counter = 0
    for members in picker_array:
        counter = counter + 1
    return counter-1

print(count_pickers(staged_df["Pickers"][100]))
"""

# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("6099") # z will be 3
# print("x is {}".format(x))

# rolls = np.random.randint(low=1, high=6, size=10)
# print(rolls+10)
# print(rolls <= 3)
# xlist = [[1,2,3],[2,4,6],]
# x = np.asarray(xlist)
# print(x[1,-1])
#print("x =\n{}".format(x))
# x=[[1,2,3],[2,4,6],[1]]
# x1 = [1]
# if x.__contains__(x1):
#     print(True)
# else:
#     print(False)

# #help(list.__contains__)
# def testA(value, count):
#     if value > 21 and count > 0:
#         value = value - 10
#         count = count - 1
#         return testA(value, count)
#     else:
#         return value


# def blackjack_hand_greater_than(hand_1, hand_2):

#     dict_value = {"A":11, "2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K": 10}
#     hand1_value = 0
#     hand2_value = 0
#     countA_1 = 0
#     countA_2 = 0

#     for i in range(len(hand_1)):
#         hand1_value = hand1_value + dict_value[hand_1[i]]
#         if hand_1[i] == "A":
#             countA_1 = countA_1 + 1
#     hand1_value = testA(hand1_value, countA_1)

#     for j in range(len(hand_2)):
#         hand2_value = hand2_value + dict_value[hand_2[j]]
#         if hand_2[j] == "A":
#             countA_2 = countA_2 + 1
#     hand2_value = testA(hand2_value, countA_2)

#     print(hand1_value, '\n',  hand2_value)
#     if ((hand1_value  <= hand2_value) and hand2_value <= 21) or (hand1_value > 21):
#         return False
#     else:
#         return True


# print(blackjack_hand_greater_than(['10', '7'], ['8', '3', 'A', '5']))        
# # Check your answer
# #q3.check()



#recursion
# Solution 1
# f = lambda n:1 if n in (1,2) else f(n-1) + f(n-2)

# Solution 2
# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a,b = b, a+b
#         print(a," ", b, '\n')
#     return a

# Solution 3
# def catche(f):
#     memo = {}
    
#     def helper(x):
#         if x not in memo:
#             memo[x] = f(x)
#             print(memo)
#             print(x)
#         return memo[x]

#     return helper

class catche(object):
    def __init__(self, f):
        super().__init__()
        self.method = f
        self.memo = {}
    def __call__(self, x):
        if x not in self.memo:
            self.memo[x] = self.method(x)
            print(self.memo)
            print(x)
        return self.memo[x]
        


# def timeit(method):
#     def timed(*args, **kw):
#         ts = time.time()
#         result = method(*args, **kw)
#         te = time.time()
#         print ('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
#         return result
#     return timed


class timeit(object):
    def __init__(self, method):
        super().__init__()
        self.method = method
    def __call__(self, *arg, **kwg):
        ts = time.time()
        result = self.method(*arg, **kwg)
        te = time.time()
        print ('%r  %2.2f ms' % (self.method.__name__, (te - ts) * 1000))
        return result

@catche
@timeit
def fibR(n):
    if n == 1 or n == 2:
        return 1
    print(n)
    return fibR(n-1) +fibR(n-2)

fibR(10)



class RandomForestRegressor(ForestRegressor):
    """
    A random forest regressor.
    A random forest is a meta estimator that fits a number of classifying
    decision trees on various sub-samples of the dataset and uses averaging
    to improve the predictive accuracy and control over-fitting.
    The sub-sample size is controlled with the `max_samples` parameter if
    `bootstrap=True` (default), otherwise the whole dataset is used to build
    each tree.
    Read more in the :ref:`User Guide <forest>`.
    Parameters
    ----------
    n_estimators : int, default=100
        The number of trees in the forest.
        .. versionchanged:: 0.22
           The default value of ``n_estimators`` changed from 10 to 100
           in 0.22.
    criterion : {"mse", "mae"}, default="mse"
        The function to measure the quality of a split. Supported criteria
        are "mse" for the mean squared error, which is equal to variance
        reduction as feature selection criterion, and "mae" for the mean
        absolute error.
        .. versionadded:: 0.18
           Mean Absolute Error (MAE) criterion.
    max_depth : int, default=None
        The maximum depth of the tree. If None, then nodes are expanded until
        all leaves are pure or until all leaves contain less than
        min_samples_split samples.
    min_samples_split : int or float, default=2
        The minimum number of samples required to split an internal node:
        - If int, then consider `min_samples_split` as the minimum number.
        - If float, then `min_samples_split` is a fraction and
          `ceil(min_samples_split * n_samples)` are the minimum
          number of samples for each split.
        .. versionchanged:: 0.18
           Added float values for fractions.
    min_samples_leaf : int or float, default=1
        The minimum number of samples required to be at a leaf node.
        A split point at any depth will only be considered if it leaves at
        least ``min_samples_leaf`` training samples in each of the left and
        right branches.  This may have the effect of smoothing the model,
        especially in regression.
        - If int, then consider `min_samples_leaf` as the minimum number.
        - If float, then `min_samples_leaf` is a fraction and
          `ceil(min_samples_leaf * n_samples)` are the minimum
          number of samples for each node.
        .. versionchanged:: 0.18
           Added float values for fractions.
    min_weight_fraction_leaf : float, default=0.0
        The minimum weighted fraction of the sum total of weights (of all
        the input samples) required to be at a leaf node. Samples have
        equal weight when sample_weight is not provided.
    max_features : {"auto", "sqrt", "log2"}, int or float, default="auto"
        The number of features to consider when looking for the best split:
        - If int, then consider `max_features` features at each split.
        - If float, then `max_features` is a fraction and
          `int(max_features * n_features)` features are considered at each
          split.
        - If "auto", then `max_features=n_features`.
        - If "sqrt", then `max_features=sqrt(n_features)`.
        - If "log2", then `max_features=log2(n_features)`.
        - If None, then `max_features=n_features`.
        Note: the search for a split does not stop until at least one
        valid partition of the node samples is found, even if it requires to
        effectively inspect more than ``max_features`` features.
    max_leaf_nodes : int, default=None
        Grow trees with ``max_leaf_nodes`` in best-first fashion.
        Best nodes are defined as relative reduction in impurity.
        If None then unlimited number of leaf nodes.
    min_impurity_decrease : float, default=0.0
        A node will be split if this split induces a decrease of the impurity
        greater than or equal to this value.
        The weighted impurity decrease equation is the following::
            N_t / N * (impurity - N_t_R / N_t * right_impurity
                                - N_t_L / N_t * left_impurity)
        where ``N`` is the total number of samples, ``N_t`` is the number of
        samples at the current node, ``N_t_L`` is the number of samples in the
        left child, and ``N_t_R`` is the number of samples in the right child.
        ``N``, ``N_t``, ``N_t_R`` and ``N_t_L`` all refer to the weighted sum,
        if ``sample_weight`` is passed.
        .. versionadded:: 0.19
    min_impurity_split : float, default=None
        Threshold for early stopping in tree growth. A node will split
        if its impurity is above the threshold, otherwise it is a leaf.
        .. deprecated:: 0.19
           ``min_impurity_split`` has been deprecated in favor of
           ``min_impurity_decrease`` in 0.19. The default value of
           ``min_impurity_split`` has changed from 1e-7 to 0 in 0.23 and it
           will be removed in 0.25. Use ``min_impurity_decrease`` instead.
    bootstrap : bool, default=True
        Whether bootstrap samples are used when building trees. If False, the
        whole dataset is used to build each tree.
    oob_score : bool, default=False
        whether to use out-of-bag samples to estimate
        the R^2 on unseen data.
    n_jobs : int, default=None
        The number of jobs to run in parallel. :meth:`fit`, :meth:`predict`,
        :meth:`decision_path` and :meth:`apply` are all parallelized over the
        trees. ``None`` means 1 unless in a :obj:`joblib.parallel_backend`
        context. ``-1`` means using all processors. See :term:`Glossary
        <n_jobs>` for more details.
    random_state : int or RandomState, default=None
        Controls both the randomness of the bootstrapping of the samples used
        when building trees (if ``bootstrap=True``) and the sampling of the
        features to consider when looking for the best split at each node
        (if ``max_features < n_features``).
        See :term:`Glossary <random_state>` for details.
    verbose : int, default=0
        Controls the verbosity when fitting and predicting.
    warm_start : bool, default=False
        When set to ``True``, reuse the solution of the previous call to fit
        and add more estimators to the ensemble, otherwise, just fit a whole
        new forest. See :term:`the Glossary <warm_start>`.
    ccp_alpha : non-negative float, default=0.0
        Complexity parameter used for Minimal Cost-Complexity Pruning. The
        subtree with the largest cost complexity that is smaller than
        ``ccp_alpha`` will be chosen. By default, no pruning is performed. See
        :ref:`minimal_cost_complexity_pruning` for details.
        .. versionadded:: 0.22
    max_samples : int or float, default=None
        If bootstrap is True, the number of samples to draw from X
        to train each base estimator.
        - If None (default), then draw `X.shape[0]` samples.
        - If int, then draw `max_samples` samples.
        - If float, then draw `max_samples * X.shape[0]` samples. Thus,
          `max_samples` should be in the interval `(0, 1)`.
        .. versionadded:: 0.22
    Attributes
    ----------
    base_estimator_ : DecisionTreeRegressor
        The child estimator template used to create the collection of fitted
        sub-estimators.
    estimators_ : list of DecisionTreeRegressor
        The collection of fitted sub-estimators.
    feature_importances_ : ndarray of shape (n_features,)
        The impurity-based feature importances.
        The higher, the more important the feature.
        The importance of a feature is computed as the (normalized)
        total reduction of the criterion brought by that feature.  It is also
        known as the Gini importance.
        Warning: impurity-based feature importances can be misleading for
        high cardinality features (many unique values). See
        :func:`sklearn.inspection.permutation_importance` as an alternative.
    n_features_ : int
        The number of features when ``fit`` is performed.
    n_outputs_ : int
        The number of outputs when ``fit`` is performed.
    oob_score_ : float
        Score of the training dataset obtained using an out-of-bag estimate.
        This attribute exists only when ``oob_score`` is True.
    oob_prediction_ : ndarray of shape (n_samples,)
        Prediction computed with out-of-bag estimate on the training set.
        This attribute exists only when ``oob_score`` is True.
    See Also
    --------
    DecisionTreeRegressor, ExtraTreesRegressor
    Notes
    -----
    The default values for the parameters controlling the size of the trees
    (e.g. ``max_depth``, ``min_samples_leaf``, etc.) lead to fully grown and
    unpruned trees which can potentially be very large on some data sets. To
    reduce memory consumption, the complexity and size of the trees should be
    controlled by setting those parameter values.
    The features are always randomly permuted at each split. Therefore,
    the best found split may vary, even with the same training data,
    ``max_features=n_features`` and ``bootstrap=False``, if the improvement
    of the criterion is identical for several splits enumerated during the
    search of the best split. To obtain a deterministic behaviour during
    fitting, ``random_state`` has to be fixed.
    The default value ``max_features="auto"`` uses ``n_features``
    rather than ``n_features / 3``. The latter was originally suggested in
    [1], whereas the former was more recently justified empirically in [2].
    References
    ----------
    .. [1] L. Breiman, "Random Forests", Machine Learning, 45(1), 5-32, 2001.
    .. [2] P. Geurts, D. Ernst., and L. Wehenkel, "Extremely randomized
           trees", Machine Learning, 63(1), 3-42, 2006.
    Examples
    --------
    >>> from sklearn.ensemble import RandomForestRegressor
    >>> from sklearn.datasets import make_regression
    >>> X, y = make_regression(n_features=4, n_informative=2,
    ...                        random_state=0, shuffle=False)
    >>> regr = RandomForestRegressor(max_depth=2, random_state=0)
    >>> regr.fit(X, y)
    RandomForestRegressor(...)
    >>> print(regr.predict([[0, 0, 0, 0]]))
    [-8.32987858]
    """
    @_deprecate_positional_args
    def __init__(self,
                 n_estimators=100, *,
                 criterion="mse",
                 max_depth=None,
                 min_samples_split=2,
                 min_samples_leaf=1,
                 min_weight_fraction_leaf=0.,
                 max_features="auto",
                 max_leaf_nodes=None,
                 min_impurity_decrease=0.,
                 min_impurity_split=None,
                 bootstrap=True,
                 oob_score=False,
                 n_jobs=None,
                 random_state=None,
                 verbose=0,
                 warm_start=False,
                 ccp_alpha=0.0,
                 max_samples=None):
        super().__init__(
            base_estimator=DecisionTreeRegressor(),
            n_estimators=n_estimators,
            estimator_params=("criterion", "max_depth", "min_samples_split",
                              "min_samples_leaf", "min_weight_fraction_leaf",
                              "max_features", "max_leaf_nodes",
                              "min_impurity_decrease", "min_impurity_split",
                              "random_state", "ccp_alpha"),
            bootstrap=bootstrap,
            oob_score=oob_score,
            n_jobs=n_jobs,
            random_state=random_state,
            verbose=verbose,
            warm_start=warm_start,
            max_samples=max_samples)

        self.criterion = criterion
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.min_weight_fraction_leaf = min_weight_fraction_leaf
        self.max_features = max_features
        self.max_leaf_nodes = max_leaf_nodes
        self.min_impurity_decrease = min_impurity_decrease
        self.min_impurity_split = min_impurity_split
        self.ccp_alpha = ccp_alpha