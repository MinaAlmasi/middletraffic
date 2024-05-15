import pathlib 
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def plot_timeseries(df, figsize:tuple=(40,10), ylim:tuple=(0,75), save_path=None, save_file=None, **kwargs):
    ts_plot = df.plot(x="ds", y="y", figsize=figsize, ylim=ylim, **kwargs)

    if save_path and save_file:
        ts_plot.get_figure().savefig(save_path / save_file)
    
    return ts_plot


def plot_decompose(df, freq:int=24, save_path=None, save_file=None):
    # decompose the timeseries
    decomp = seasonal_decompose(df['y'], period=freq)

    # plot the decomposed timeseries
    decomp_plot = decomp.plot()
    decomp_plot.set_size_inches((40, 10))

    if save_path and save_file:
        decomp_plot.get_figure().savefig(save_path / save_file)

    return decomp_plot

def main():
    # set paths
    path = pathlib.Path(__file__)
    data_path = path.parents[1] / "data"
    plot_dir = path.parents[1] / "plots" / "graphical_analysis"

    # load data
    df = pd.read_csv(data_path / "processed_1A_norreport.csv")

    # plot the timeseries for Cumulative
    plot_timeseries(df, figsize=(40,10), ylim=(0,75), save_path=plot_dir, save_file="norreport_1A_ts.png")

    # create another plot that is zoomed into the last two month (24 hours x 30 days * 2 months)
    df_recent = df.tail(2*24*30)
    plot_timeseries(df_recent, figsize=(25,10), ylim=(0,70), save_path=plot_dir, save_file="norreport_1A_ts_recent.png")

    # create another that is just the last two days
    df_two_days = df.tail(2*24)
    plot_timeseries(df_two_days, figsize=(15,10), ylim=(0,60), save_path=plot_dir, save_file="norreport_1A_ts_two_days.png", linewidth=2)
    
    # plot the decomposed timeseries
    plot_decompose(df, freq=24, save_path=plot_dir, save_file="norreport_1A_decompose.png")

    # plot the decomposed timeseries for the last two days
    plot_decompose(df_recent, freq=24, save_path=plot_dir, save_file="norreport_1A_decompose_recent.png")

if __name__ == "__main__":
    main()