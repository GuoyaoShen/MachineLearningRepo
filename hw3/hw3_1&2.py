# -*- coding: utf-8 -*-
"""hw3_1&2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h2mhqA2B38MZr2Wo3lmTM74RmpA-v5wx

# **Problem 1: Regularization Penalties**
"""

import numpy as np
import pickle
import sklearn.linear_model as LR

# load data
from google.colab import files
uploaded = files.upload()

with open('q1.pkl', 'rb') as f:
    data = pickle.load(f)
print(type(data))
print(data.keys())
print(data['x'].shape)
print(data['y'].shape)

"""### (1) No Penality"""

model = LR.LinearRegression(fit_intercept=False)
X = data['x']
y = data['y']
reg = model.fit(X, y)
preds = reg.predict(X)
w = reg.coef_  #(1,p)

# now calcul closed form w
w_closed = np.linalg.pinv(X.T @ X) @ (X.T@y)

print('w.SHAPE', w.shape)
print('w', w)
print('w_closed', w_closed)

"""### (2) L2 Penality"""

model = LR.Ridge(alpha=1., fit_intercept=False)
X = data['x']
y = data['y']
reg = model.fit(X, y)
preds = reg.predict(X)
w = reg.coef_  #(1,p)

# now calcul closed form w
w_closed = np.linalg.pinv(X.T @ X + 1.*np.eye(X.shape[1])) @ (X.T@y)

print('w.SHAPE', w.shape)
print('w', w)
print('w_closed', w_closed)

"""### (3) L1 Penality"""

model = LR.Lasso(alpha=1., fit_intercept=False)
X = data['x']
y = data['y']
reg = model.fit(X, y)
preds = reg.predict(X)
w = reg.coef_  #(p,)
print('w.SHAPE', w.shape)
print('w', w)

"""### (4) L0 Penality:
just search around all 0-non0 combinations of wi
"""

def norm0(X):
    score = np.where(X!=0, 1, 0)
    norm = np.sum(score)
    return norm


def OLS_L0(lambdaa, X, y, w):
    '''
    X: (n,p)
    y: (n,1)
    w: (1,p)
    '''
    error = (np.linalg.norm(y - X@w.T))**2 + lambdaa*norm0(w)
    return error

# [0 0 0]
X_all = data['x']  #(50,3)
y_all = data['y']  #(50,1)

w_all = np.zeros((1,3))
error0 = OLS_L0(1, X_all, y_all, w_all)
print('error0', error0)


# [w1 0 0]

# [0 w2 0]

# [0 0 w3]

# [w1 w2 0]

# [w1 0 w3]

# [0 w2 w3]

# [w1 w2 w3]

# [w1 0 0]
X1 = X_all[:,0]
X1 = X1[:, np.newaxis]
print('X.SHAPE', X1.shape)
y1 = data['y']

model = LR.LinearRegression(fit_intercept=False)
reg = model.fit(X1, y1)
w = reg.coef_  #(1,p)
print('w.SHAPE', w.shape)
print('w', w)

error0 = OLS_L0(1, X1, y1, w)
print('error0', error0)

# [0 w2 0]
X2 = X_all[:,1]
X2 = X2[:, np.newaxis]
print('X.SHAPE', X2.shape)
y2 = data['y']

model = LR.LinearRegression(fit_intercept=False)
reg = model.fit(X2, y2)
w = reg.coef_  #(1,p)
print('w.SHAPE', w.shape)
print('w', w)

error0 = OLS_L0(1, X2, y2, w)
print('error0', error0)

# [0 0 w3]
X3 = X_all[:,2]
X3 = X3[:, np.newaxis]
print('X.SHAPE', X3.shape)
y3 = data['y']

model = LR.LinearRegression(fit_intercept=False)
reg = model.fit(X3, y3)
w = reg.coef_  #(1,p)
print('w.SHAPE', w.shape)
print('w', w)

error0 = OLS_L0(1, X3, y3, w)
print('error0', error0)

# [w1 w2 0]
X4 = X_all[:,0:2]
print('X.SHAPE', X4.shape)
y4 = data['y']

model = LR.LinearRegression(fit_intercept=False)
reg = model.fit(X4, y4)
w = reg.coef_  #(1,p)
print('w.SHAPE', w.shape)
print('w', w)

error0 = OLS_L0(1, X4, y4, w)
print('error0', error0)

# [w1 0 w3]
X5 = X_all[:,0:3:2]
print('X.SHAPE', X5.shape)
y5 = data['y']

model = LR.LinearRegression(fit_intercept=False)
reg = model.fit(X5, y5)
w = reg.coef_  #(1,p)
print('w.SHAPE', w.shape)
print('w', w)

error0 = OLS_L0(1, X5, y5, w)
print('error0', error0)

# [0 w2 w3]
X6 = X_all[:,1:3]
print('X.SHAPE', X6.shape)
y6 = data['y']

model = LR.LinearRegression(fit_intercept=False)
reg = model.fit(X6, y6)
w = reg.coef_  #(1,p)
print('w.SHAPE', w.shape)
print('w', w)

error0 = OLS_L0(1, X6, y6, w)
print('error0', error0)

# [w1 w2 w3]
X7 = data['x']
print('X.SHAPE', X7.shape)
y7 = data['y']

model = LR.LinearRegression(fit_intercept=False)
reg = model.fit(X7, y7)
w = reg.coef_  #(1,p)
print('w.SHAPE', w.shape)
print('w', w)

error0 = OLS_L0(1, X7, y7, w)
print('error0', error0)

"""## (6)

### (6).(a)
"""

model = LR.LinearRegression(fit_intercept=False)
X = data['x']  #(50,3)
y = data['y']  #(50,1)
reg = model.fit(X, y)
preds = reg.predict(X)
w = reg.coef_  #(1,p)
print('w.SHAPE', w.shape)
print('w', w)

up = np.linalg.norm(w)**2
down = np.linalg.norm(y-X@w.T)**2
ratio = 1.0*up/down
print('ratio', ratio)

"""### (6).(c)"""

# calculate w MLE
model = LR.LinearRegression(fit_intercept=False)
X = data['x']  #(50,3)
y = data['y']  #(50,1)
reg = model.fit(X, y)
preds = reg.predict(X)
w_MLE = reg.coef_  #(1,p)

# calculate w with Ridge Regression
while 1:
    lambdaa = np.random.rand(1)*100.
    
    
    model = LR.Ridge(alpha=lambdaa, fit_intercept=False)
    reg = model.fit(X, y)
    preds = reg.predict(X)
    w_R = reg.coef_  #(1,p)
    
    ratio = np.linalg.norm(w_R)**2 / np.linalg.norm(w_MLE)**2
#     print('ratio', ratio)
    
    if (ratio>0.8) and (ratio<0.9):
        print('chosen lambda:', lambdaa)
        break

"""### (6).(d)"""

# calculate w MLE
model = LR.LinearRegression(fit_intercept=False)
X = data['x']  #(50,3)
y = data['y']  #(50,1)
reg = model.fit(X, y)
preds = reg.predict(X)
w_MLE = reg.coef_  #(1,p)

# calculate w with Ridge Regression
while 1:
    lambdaa = np.random.rand(1)*100.
    
    
    model = LR.Ridge(alpha=lambdaa, fit_intercept=False)
    reg = model.fit(X, y)
    preds = reg.predict(X)
    w_R = reg.coef_  #(1,p)
    
    ratio = np.linalg.norm(w_R)**2 / np.linalg.norm(w_MLE)**2
#     print('ratio', ratio)
    
    if (ratio>0.4) and (ratio<0.5):
        print('chosen lambda:', lambdaa)
        break

"""# **Problem 2: Feature Selection**"""

import numpy as np
from sklearn.linear_model import LinearRegression

y = np.array([[1.], [9.], [4.]])  #(3,1), (n,1)
X_all = np.array([[1, 2, 1.3], [2, 1, 7.3], [1, 1, 2.8]])  #(3,3), (n, p)
X1 = np.array([[1.], [2.], [1.]])  #(3,1)
X2 = np.array([[2.], [1.], [1.]])  #(3,1)
X3 = np.array([[1.3], [7.3], [2.8]])  #(3,1)

model = LinearRegression(fit_intercept=False)
reg = model.fit(X, y)
preds = reg.predict(X)
w = reg.coef_  #(1,p)
print(w.shape)

def norm0(X):
    score = np.where(X!=0, 1, 0)
    norm = np.sum(score)
    print('L0 norm', norm)
    return norm


def OLS_L0(lambdaa, X, y, w):
    '''
    X: (n,p)
    y: (n,1)
    w: (1,p)
    '''
    error = (np.linalg.norm(y - X@w.T))**2 + lambdaa*norm0(w)
    return error

"""### Streamwise Regression"""

# # calculate error0
# w0 = np.zeros((1,3))
# error0 = OLS_L0(0.2, X_all, y, w0)
# print('error0:', error0)

# # streamwise order 1,2,3
# print('ORDER 1 2 3')
# model = LinearRegression(fit_intercept=False)
# for i in range(3):
#     X = X_all[:, :i+1]
    
#     # calculate w
# #     model = LinearRegression(fit_intercept=False)
#     reg = model.fit(X, y)
#     preds = reg.predict(X)
#     w = reg.coef_  #(1,p)
#     print('w.SHAPE', w.shape)
    
#     # calculate error
#     error = OLS_L0(0.2, X, y, w)
#     print('error'+str(i+1)+': '+str(error))
#     print('w:', reg.coef_)
# print('============================================')



# streamwise order 1,2,3
print('ORDER 1 2 3')
model = LinearRegression(fit_intercept=False)
error_old = error0
list_order = [1, 2, 3]
for i in range(3):
#     X = X_all[:, -1:-(i+2):-1]
    if i == 0:
        X = X_all[:, list_order[i]-1]
        X = X[:, np.newaxis]
    else:
        X_added = X_all[:, list_order[i]-1]
        X_added = X_added[:, np.newaxis]
        X = np.concatenate((X,X_added), axis=1)
    print('X.SHAPE', X.shape)
    
    # calculate w
#     model = LinearRegression(fit_intercept=False)
    reg = model.fit(X, y)
    preds = reg.predict(X)
    w = reg.coef_  #(1,p)
    print('w.SHAPE', w.shape)
    
    # calculate error
    error = OLS_L0(0.2, X, y, w)
    print('error'+str(i+1)+': '+str(error))
    print('w:', reg.coef_)
    
    if error>= error_old:
        X = X[:, :-1]
        print('NEW X.SHAPE', X.shape)
    else:
        error_old = error
    print('error_old', error_old)
    
    print('---------------')
print('============================================')



# streamwise order 3,2,1
print('ORDER 3 2 1')
model = LinearRegression(fit_intercept=False)
error_old = error0
list_order = [3, 2, 1]
for i in range(3):
#     X = X_all[:, -1:-(i+2):-1]
    if i == 0:
        X = X_all[:, list_order[i]-1]
        X = X[:, np.newaxis]
    else:
        X_added = X_all[:, list_order[i]-1]
        X_added = X_added[:, np.newaxis]
        X = np.concatenate((X,X_added), axis=1)
    print('X.SHAPE', X.shape)
    
    # calculate w
#     model = LinearRegression(fit_intercept=False)
    reg = model.fit(X, y)
    preds = reg.predict(X)
    w = reg.coef_  #(1,p)
    print('w.SHAPE', w.shape)
    
    # calculate error
    error = OLS_L0(0.2, X, y, w)
    print('error'+str(i+1)+': '+str(error))
    print('w:', reg.coef_)
    
    if error>= error_old:
        X = X[:, :-1]
        print('NEW X.SHAPE', X.shape)
    else:
        error_old = error
    print('error_old', error_old)
    
    print('---------------')
print('============================================')

"""### Stepwise Regression"""

# calculate error0
w0 = np.zeros((1,3))
error0 = OLS_L0(0.2, X_all, y, w0)
print('error0:', error0)

error_old = error0

N = X_all.shape[0]
P = X_all.shape[1]

idx_feature = 10

# do stepwise reegression
for i in range(P):
    
    print('ERROR_OLD =', error_old)
    
    
    # search around all features
    list_error = np.ones((P,))*1000
    for k in range(P):
        
        if i==0:
            Xi = X_all[:, k]
            Xi = Xi[:, np.newaxis]
        
        if k!= idx_feature-1:  # not selected festure
            xk = X_all[:, k]
            xk = xk[:, np.newaxis]
#             if i==0:
#                 Xi = xk
            if i != 0:
                Xi_old = Xi
                Xi = np.concatenate((Xi, xk), axis=1)
        
            # calculate w
            model = LinearRegression(fit_intercept=False)
            print('XI.SHAPE', Xi.shape)
            reg = model.fit(Xi, y)
            preds = reg.predict(Xi)
            w = reg.coef_  #(1,p)
        
            # calculate error
            error = OLS_L0(0.2, Xi, y, w)
            list_error[k] = error
            print('The current Err for xi='+str(k+1)+' is: '+str(error))
            
            if i != 0:
                Xi = Xi_old
        
    error_new = np.amin(list_error)
    
    if error_new < error_old:
        error_old = error_new
        idx_feature = np.argmin(list_error)+1
        
        # concat the minimum element
        if i==0:
            Xi = X_all[:, idx_feature-1]
            Xi = Xi[:, np.newaxis]
        else:
            X_cat = X_all[:, idx_feature-1]
            X_cat = X_cat[:, np.newaxis]
            Xi = np.concatenate((Xi, X_cat), axis=1)
        
        
#         X_cat = X_all[:, idx_feature-1]
#         X_cat = X_cat[:, np.newaxis]
#         Xi = np.concatenate((Xi, X_cat), axis=1)
        print('NEW XI.SHAPE', Xi.shape)
        
        print('The '+str(i+1)+'th feature is feature'+str(idx_feature))
        print('-----------------------------')
    else:
        break
        
#         xk = X_all[:, k]
#         xk = xk[:, np.newaxis]
#         if i==0:
#             Xi = xk
#         else:
#             Xi = np.concatenate((Xi, xk), axis=1)
        
#         # calculate w
#         model = LinearRegression(fit_intercept=False)
#         reg = model.fit(Xi, y)
#         preds = reg.predict(Xi)
#         w = reg.coef_  #(1,p)
        
#         # calculate error
#         error = OLS_L0(0.2, Xi, y, w)
#         list_error[k] = error
#         print('The current Err for xi='+str(k+1)+' is: '+str(error))
        
#     error_new = np.amin(list_error)
    
#     if error_new < error_old:
#         error_old = error_new
#         idx_feature = np.argmin(list_error)+1
#         print('The '+str(i+1)+'th feature is feature'+str(idx_feature))