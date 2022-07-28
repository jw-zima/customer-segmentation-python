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


def plot_boxplot_by_cluster(df, num_var, cluster_var, outliers_to_remove=None):
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
    # print(num_var)
    if not(pd.isnull(outliers_to_remove)):
        if (type(outliers_to_remove) == float):
            quantiles = df[num_var].quantile([outliers_to_remove,
                                              1 - outliers_to_remove])
            df = df.loc[((df[num_var] > quantiles.iloc[0])
                        & (df[num_var] < quantiles.iloc[1])), :]
    try:
        g = (ggplot(df)
             + geom_boxplot(aes(x=cluster_var, y=num_var, fill=cluster_var))
             + ggtitle(num_var)
             + theme_light()
             + scale_fill_brewer(type="qual", palette="Dark2"))
        return print(g)
    except Exception:
        pass


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
                                  fill=cluster_var))
                 + ggtitle(num_var1 + " vs " + num_var2)
                 + theme_light()
                 + scale_fill_brewer(type="qual", palette="Dark2"))


def plot_share_of_binary_vars_per_clusters(df, var, cluster_var):
    """Make a column plot colored by clusters using ggplot grammar of graphics
    to present share of given binery var in each cluster

    Args:
    df (data.frame): dataset
    var (string): name of variable for x axis
    cluster_var (string): name of variable with clustes

    Yields:
    plot: Column plot with share of both binaries per cluster

    Examples:
    >>> plot_share_of_binary_vars_per_clusters(dataset, "education_cleaned",
                                               "cluster_kmeans")
    """
    df = df.loc[:, [var, cluster_var]]
    df = df.groupby([var, cluster_var]).value_counts()
    df = df.reset_index().rename(columns={0: 'n'})
    df['n_cluster'] = df.groupby(['cluster_kmeans']).n.transform('sum')
    df['share_in_cluster'] = round(100 * df['n'] / df['n_cluster'], 1)

    g = (ggplot(df)
         + geom_col(aes(x=var, y="share_in_cluster", fill=cluster_var))
         + facet_wrap('~' + cluster_var)
         + theme_light()
         + theme(legend_position="top")
         + theme(axis_text_x=element_text(rotation=90, hjust=1))
         + scale_fill_brewer(type="qual", palette="Dark2"))
    print(g)


def plot_stacked_vars_per_clusters(df, vars_list, cluster_var):
    """Make a stacked column plot colored by variable using ggplot grammar
    of graphics split by clusters

    Args:
    df (data.frame): dataset
    vars_list (list): list of names of numeric variables that should be stacked
    cluster_var (string): name of variable with clustes

    Yields:
    plot: Stacked column plot with mean value of each numeric variable
    from the list per cluster

    Examples:
    >>> plot_stacked_vars_per_clusters(dataset,
    ["wines_share", "fruits_share", "meat_share", "fish_share", "sweets_share",
    "gold_products_share"], "cluster_kmeans")
    """
    vars_list.append("cluster_kmeans")
    df = df.loc[:, vars_list]
    df = df.groupby("cluster_kmeans").agg(['mean'])
    df = df.unstack().reset_index()
    df.columns = ['variable', 'agg_function', 'cluster_kmeans', 'mean_value']
    df = df.drop('agg_function', axis=1)

    return print(ggplot(x, aes(fill="variable", y="mean_value",
                               x="cluster_kmeans"))
                 + geom_bar(position="fill", stat="identity")
                 + theme_light()
                 + scale_fill_brewer(type="qual", palette="Dark2"))
