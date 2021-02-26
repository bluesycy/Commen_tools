#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### Do PCA

# Center the data

r = r - np.outer(np.ones(len(t)), np.mean(r,0))

# Compute covariance matrix

C = np.dot(r.T, r) / len(t)

# Compute eigenvectors

V = np.linalg.eigh(C)[1]

#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### Plot activity in the first 3 PC

fig = plt.figure()
ax = plt.axes(projection='3d')

# Plot every int_t = 10 steps
int_t = 10
ax.plot(np.dot(r[::int_t,:], V[:,-1]), np.dot(r[::int_t,:], V[:,-2]), np.dot(r[::int_t,:], V[:,-3]), '-o',color = '0.5')

plt.rcParams['axes.labelpad'] = 0.1
ax.dist = 12

ax.grid('off')

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')

plt.show()
