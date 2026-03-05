import matplotlib.pyplot as plt
import seaborn as sns

def plot_mh_distribution(df, cols, palette='viridis'):
    """
    Plots the distribution of multiple mental health score columns side-by-side.
    """
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, len(cols), figsize=(15, 4))
    
    for i, col in enumerate(cols):
        sns.histplot(df[col], kde=True, ax=axes[i], color=sns.color_palette(palette)[i], bins=10)
        axes[i].set_title(f'Distribution of {col} Scores')
        axes[i].set_xlabel(f'{col} Score (0-10)')
        axes[i].set_ylabel('Frequency')
        
    plt.tight_layout()
    plt.show()

def plot_genre_vs_mh(df, genre_col, mh_col):
    """
    Creates a horizontal boxplot sorted by median to visualize the relationship 
    between favorite music genre and a specific mental health score.
    """
    plt.figure(figsize=(10, 8)) 
    
    # Sort genres by median MH score
    order = df.groupby(genre_col)[mh_col].median().sort_values(ascending=False).index
    
    sns.boxplot(data=df, x=mh_col, y=genre_col, order=order, palette='pastel', hue=genre_col, legend=False)
    
    plt.title(f'{mh_col} Scores Across Different {genre_col}s', fontsize=14)
    plt.xlabel(f'{mh_col} Score (0-10)', fontsize=12)
    plt.ylabel('Favorite Genre', fontsize=12)
    plt.xlim(0, 10)
    plt.tight_layout()
    plt.show()