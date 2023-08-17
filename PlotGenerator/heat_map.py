import numpy as np
import matplotlib.pylab as plt
import matplotlib
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors
import matplotlib.patches as patches
import csv


def read_data(file):
    with open(file, 'r') as txt_files:
        i = 0
        data = []
        for line in txt_files:
            data.append(line.split(","))
    return data

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw=None, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
#    im = ax.imshow(data, **kwargs, origin = 'lower')
    im = ax.imshow(data, **kwargs)



    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_xticklabels(col_labels)
    ax.set_yticks(np.arange(data.shape[0]))
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=False, bottom=True,
                   labeltop=False, labelbottom=True)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=0,
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    #ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.set_axisbelow(True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.add_patch(
    patches.Rectangle(xy=(2.5, -1.5), width=4, height=5, linewidth=3,  color='red', fill=False))
    ax.tick_params(which="minor", bottom=False, left=False)
    ax.set_xlabel("Average last_use (number of windows)")
    ax.set_ylabel("Accesses (number of windows)")

        # Create colorbar
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.2)
    
    cbar = ax.figure.colorbar(im, cax=cax)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None,text=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            if text is not None:
                if i == data.shape[0]-1 and j>0:
                    textt = im.axes.text(j, i, "n.a", **kw)
                else:
                    textt = im.axes.text(j, i, text[i, j], **kw)
            else:
                if i == data.shape[0]-1 and j>0:
                    textt = im.axes.text(j, i, "n.a", **kw)
                else:
                    textt = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

dir_path = os.path.dirname(os.path.realpath(__file__))
data_file = dir_path + "/../Data/ProcessedData/last_use_vector.txt"
plot_file = dir_path + "/../Data/PlotData/scatter_lastuse_access.pdf"
data = read_data(data_file)
matrix = np.zeros((7,6))
nb_data = 0
avg_last_use = 0
avg_transaction = 0
nb_unfriendly = 0
for x in data:
    coord = [0,0]
    nb_data += 1
    if float(x[1]) <= 1:
        coord[0] = 6
    elif float(x[1]) <= 2:
        coord[0] = 5
    elif float(x[1]) <= 3:
        coord[0] = 4
    elif float(x[1]) <= 5:
        coord[0] = 3
    elif float(x[1]) <= 10:
        coord[0] = 2
    elif float(x[1]) <= 20:
        coord[0] = 1
    else:
        coord[0] = 0

    if float(x[2]) <= 0.5:
        coord[1] = 0
    elif float(x[2]) <= 1:
        coord[1] = 1
    elif float(x[2]) <= 3:
        coord[1] = 2
    elif float(x[2]) <= 5:
        coord[1] = 3
    elif float(x[2]) <= 10:
        coord[1] = 4
    else:
        coord[1] = 5
    matrix[coord[0], coord[1]] = matrix[coord[0], coord[1]] + 1

    if coord[1] >= 3:
        nb_unfriendly += 1
        avg_last_use += float(x[2])
        avg_transaction += float(x[1])

print("nb unfriendly:", nb_unfriendly)
print("avg last use:", avg_last_use/nb_unfriendly)
print("avg tx:", avg_transaction/nb_unfriendly)

matrix = matrix / nb_data
matrix = matrix * 100
print(nb_data)
with open("data.csv",'w') as output_file:
    fieldnames = ['0','1','2','3','4','5']
    dict_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    dict_writer.writeheader()
    for x in range(7):
        record = {}
        for y in range(6):
            record[str(y)] = matrix[x,y]
        dict_writer.writerow(record)
print("done")

last_use = ["[0,0.5]\n ", "]0.5,1]\n ", "]1,3]\n ", "]3,5]\n ", "]5,10]\n", ">10\n "]
nb_access = [">20\n ", "[11,20]\n ", "[6,10]\n ", "[4,5]\n", "3\n ", "2\n ", "1\n "]

fig, ax = plt.subplots(figsize=(5, 5))

im, cbar = heatmap(matrix, nb_access, last_use, ax=ax,
                   cmap="Greys", norm=colors.PowerNorm(gamma = 0.4), cbarlabel="% of accounts")
texts = annotate_heatmap(im, valfmt="{x:.1f}", threshold=4)

plt.tight_layout()
plt.savefig(plot_file, format = "pdf")
#plt.show()