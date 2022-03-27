import numpy as np # numpy is commonly used to process number array

x = np.array(([2, 7], [1, 2], [3, 6]), dtype=float) # Features ( Hrs Slept, Hrs Studied) 
y = np.array(([92], [86], [89]), dtype=float)	# Labels(Marks obtained)

x = x/np.amax(x,axis=0) # Normalize 
y = y/100

def sigmoid(x):
    return 1/(1 + np.exp(-x))
def grad(x):
    return x * (1 - x)

# Variable initialization
epic=3	#Setting training iterations
epic1 =0.2		#Setting learning rate (eta)
input_neurons = 2	#number of features in data set 
hidden_neurons = 3	#number of hidden layers neurons
output_neurons = 1	#number of neurons at output layer

# Weight and bias - Random initialization
wh=np.random.uniform(size=(input_neurons,hidden_neurons))	# 2x3 
bh=np.random.uniform(size=(1,hidden_neurons))	# 1x3 
wout=np.random.uniform(size=(hidden_neurons,output_neurons)) # 1x1 
bout=np.random.uniform(size=(1,output_neurons))

for i in range(epic):
#Forward Propogation
    hip=np.dot(x,wh) + bh	# Dot product + bias 
    hact = sigmoid(hip)	# Activation function 
    oip=np.dot(hact,wout) + bout
    oact = sigmoid(oip)

#Backpropagation
    # Error at Output layer
    Eo = y-oact	# Error at o/p 
    
    outgrad = grad(Eo)
    d_output = Eo* outgrad	# Errj=Oj(1-Oj)(Tj-Oj)

    # Error at Hidden later
    Eh = d_output.dot(wout.T)	# .T means transpose
    hiddengrad = grad(Eh)	# How much hidden layer wts contributed to error 
    d_hidden = Eh * hiddengrad
    wout += hact.T.dot(d_output) *epic1	# Dotproduct of nextlayererror and currentlayerop 
    wh += x.T.dot(d_hidden) *epic1
 
print("Normalized Input: " + str(x))
print("Actual Output: " + str(y))
print("Predicted Output:" ,oact)
