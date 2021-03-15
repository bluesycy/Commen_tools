# * set root to the location where you downloaded the data *
root      = 'D:/grive/cshl_suite2p/TX39/'

# LOAD the visual stimuli "mov" and the timings "iframe"
mov    = np.load(os.path.join(root, 'mov.npy')) # these are the visual stimuli shown
iframe = np.load(os.path.join(root, 'iframe.npy')) # iframe[n] is the microscope frame for the image frame n
