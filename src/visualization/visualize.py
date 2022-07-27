"""UDFs for visualization

This script contains user defined functions useful for visualization
"""

import pandas as pd
from plotnine import *


def highlight_elbow_row(df, elbow, column):
    """Return dataframe containing cluster stats with highlighted selected
    number of clusters

    Args:
        df (data.frame): dataset with clustering stats
        elbow (int): selected number of clusters
        column (string): name of variable containing number of clusters

    Yields:
        plot: a formatted data frame

    Examples:
        >>> data.style.apply(highlight_elbow_row, elbow = 5,
        column = 'nb_clusters', axis=1)
    """
    is_selected = pd.Series(data=False, index=df.index)
    is_selected[column] = ((df.loc[column] >= elbow)
                           & (df.loc[column] <= (elbow)))
    return ['background-color: green' if is_selected.any()
            else '' for v in is_selected]


def draw_line_plot_for_each_k(df, x_var, y_var):
    """Make a line plot using ggplot grammar of graphics

    Args:
        df (data.frame): dataset
        x_var (string): name of variable for x axis
        y_var (string): name of variable for y axis

    Yields:
        plot: Line plot with also marked points

    Examples:
        >>> draw_line_plot_for_each_k(dataset, "nb_clusters", "error")
    """
    return (ggplot(df)
            + geom_line(aes(x=x_var, y=y_var))
            + geom_point(aes(x=x_var, y=y_var))
            + ggtitle(y_var + " for selected k")
            + theme_light()
            + scale_x_continuous(breaks=df[x_var]))


def plot_boxplot_by_cluster(df, num_var, cluster_var):
    """Make a box plot for each cluster using ggplot grammar of graphics

    Args:
    df (data.frame): dataset
    num_var (string): name of numeric variable for density estimation
    cluster_var (string): name of variable with clustes

    Yields:
    plot: Density plot for distributions from all clusters

    Examples:
    >>> plot_boxplot_by_cluster(dataset, "age", "cluster_kmeans")
    """
    return print(ggplot(df)
                 + geom_boxplot(aes(x=cluster_var, y=num_var,
                                    fill=cluster_var))
                 + ggtitle(num_var)
                 + theme_light())


def plot_scatter_by_cluster(df, num_var1, num_var2, cluster_var):
    """Make a scatter plot colored by clusters using ggplot grammar of graphics

    Args:
    df (data.frame): dataset
    num_var1 (string): name of variable for x axis
    num_var2 (string): name of variable for y axis
    cluster_var (string): name of variable with clustes

    Yields:
    plot: Density plot with overlaping distributions

    Examples:
    >>> plot_scatter_by_cluster(dataset, "age",
                                "total_purchases", "cluster_kmeans")
    """
    return print(ggplot(df)
                 + geom_point(aes(x=num_var1, y=num_var2,
                                  color=cluster_var))
                 + ggtitle(num_var1 + " vs " + num_var2)
                 + theme_light())
