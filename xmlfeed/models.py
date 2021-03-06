
import feedparser
import pandas as pd


class ProductFeed:
    def __init__(self, feed: feedparser.FeedParserDict):
        self.feed = feed
        self.df_entries = pd.DataFrame(data=feed.entries)
        self.nr_of_items = len(self.df_entries)
        self.nr_of_in_stock_items = self.count_in_stock_items(self.df_entries)

    @staticmethod
    def count_in_stock_items(df: pd.DataFrame):
        """
        :return: Sum of in stock items or "" if no 'g_availability' tag
        """
        nr_of_items_in_stock = ""
        if 'g_availability' in df.columns:
            nr_of_items_in_stock = sum(df['g_availability'] == 'in stock')
        return nr_of_items_in_stock

    def _get_labels_data(self, custom_label):
        entries_groupby_result = self.df_entries.groupby(custom_label)

        labels_data = []
        for label_name, df_label_details in entries_groupby_result:
            if label_name:
                nr_of_items = len(df_label_details)
                nr_of_items_in_stock = self.count_in_stock_items(df_label_details)
                label_values = {'label_name': label_name,
                                'nr_of_items': nr_of_items,
                                'nr_of_items_in_stock': nr_of_items_in_stock}
                labels_data.append(label_values)

        return labels_data

    def get_custom_labels_data(self):
        custom_labels = [col
                         for col in self.df_entries.columns.to_list()
                         if 'custom_label' in col]

        custom_labels_data = []
        for custom_label in custom_labels:
            custom_label_values_list = self._get_labels_data(custom_label)

            label_dict = {'custom_label': custom_label,
                          'custom_label_values': custom_label_values_list}
            custom_labels_data.append(label_dict)

        return custom_labels_data
