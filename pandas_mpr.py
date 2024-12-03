#!/usr/bin/env python
# coding: utf-8

# In[3]:


class CustomPandas:
    @staticmethod
    def read_csv(filename):
        # Custom implementation of reading CSV
        data = []
        with open(filename, 'r') as file:
            for line in file:
                data.append(line.strip().split(','))
        return data

    @staticmethod
    def drop(df, columns, axis=0):
        # Custom implementation of dropping columns
        if isinstance(df, list):
            if axis == 0:
                return [row for i, row in enumerate(df) if i not in columns]
            elif axis == 1:
                return [[val for j, val in enumerate(row) if j != columns] for row in df]
        else:  # Assume DataFrame
            return df.drop(columns=columns, axis=axis)

    @staticmethod
    def values(df):
        # Custom implementation of getting DataFrame values
        if isinstance(df, list):
            return df
        else:  # Assume DataFrame
            return df.values.tolist()

    @staticmethod
    def reshape(df, shape):
        # Custom implementation of reshaping DataFrame
        if isinstance(df, list):
            return [df[i * shape[1]:(i + 1) * shape[1]] for i in range(len(df) // shape[1])]
        else:  # Assume DataFrame
            return df.values.reshape(shape).tolist()

    @staticmethod
    def to_dataframe(data):
        # Custom implementation to convert list to DataFrame
        num_cols = len(data[0])
        col_names = [f"col_{i}" for i in range(num_cols)]
        df_dict = {col_name: [] for col_name in col_names}

        for row in data:
            for i, val in enumerate(row):
                df_dict[f"col_{i}"].append(val)

        return df_dict


# In[ ]:




