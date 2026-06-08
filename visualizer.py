"""
VISUALIZER.PY

Shows the analysis in the terminal.
"""
import matplotlib.pyplot as plt

def visualize(df, df_name, shape, numeric_columns, corr_matrix):
    print(f"The dataframe's shape is: \n Rows: {shape[0]}\n Columns: {shape[1]}\n")
    print("-"*25)
    print("\n")
    print(f"Numeric columns are: \n")
    for column in numeric_columns:
        print(column)
    print("\n")
    print("-"*25)
    print("\n")
    print("Analyzing and creating figures...")
    print("\n")
    print("-"*25)

    for column in numeric_columns:
        #if "id" not in column:
            plt.hist(df[column], bins=10)
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.title(f"{column} Distribution")
            figname = str(df_name + "__" + column + ".jpg")
            plt.savefig("outputs/histograms/"+figname, dpi=300, bbox_inches='tight')
            plt.close()


    plt.figure(figsize=(10, 8))
    plt.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)
    plt.colorbar()
    columns = corr_matrix.columns
    plt.xticks(range(len(columns)), columns, rotation=45, ha='right')
    plt.yticks(range(len(columns)), columns)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    figname = str(df_name + "__Correlation Matrix.jpg")
    plt.savefig("outputs/correlations/"+figname, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()


