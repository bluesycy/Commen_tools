### Plot configuration

fig_width = 4.2 # width in inches
fig_height = 3.  # height in inches
fig_size =  [fig_width,fig_height]
plt.rcParams['figure.figsize'] = fig_size
plt.rcParams['figure.autolayout'] = True
plt.rcParams['font.size'] = 12
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False


plt.eventplot(interval_spike_times[neuron_idx], color=".2")


_ = widgets.interact(Myplot_E_diffI_difftau, I_ext=(0.0, 10., 1.),
                     tau=(1., 5., 0.2))


##seaborn
import pandas as pd
d = {'Normalized firing rate': firing_list, 'pext': pext_list,
     'p0':self_excitation_list}
df = pd.DataFrame(data=d)
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(dpi=250)
# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="pext", y="Normalized firing rate",
            hue="p0", palette=["m", "g","r"],
            data=df)
plt.axhline(1,linestyle='dashed',color='gray')
# sns.despine(offset=10, trim=True)
