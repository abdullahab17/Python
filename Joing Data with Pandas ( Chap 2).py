import pandas as pd

movies = pd.read_pickle('Datasets/movies.p')
financials = pd.read_pickle('Datasets/financials.p')
# Merge the movies' table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)
print('-----------------------------------------------\n')

# toy_story = pd.read_pickle('Datasets/')
# # Merge the toy_story and taglines tables with a left join
# toystory_tag = toy_story.merge(taglines, on='id',how = 'left')
#
# # Print the rows and shape of toystory_tag
# print(toystory_tag)
# print(toystory_tag.shape)
#
# # Merge the toy_story and taglines tables with a inner join
# toystory_tag = toy_story.merge(taglines, on='id')
#
# # Print the rows and shape of toystory_tag
# print(toystory_tag)
# print(toystory_tag.shape)
print('-----------------------------------------------\n')

# action_movies = pd.read_pickle('Datasets/action_movies.p')
# # Merge action_movies to the scifi_movies with right join
# action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
#                                    suffixes=('_act','_sci'))
#
# # From action_scifi, select only the rows where the genre_act column is null
# scifi_only = action_scifi[action_scifi['genre_act'].isnull()]
#
# # Merge the movies and scifi_only tables with an inner join
# movies_and_scifi_only = movies.merge(scifi_only, how='inner',left_on ='id', right_on='movie_id')
#
# # Print the first few rows and shape of movies_and_scifi_only
# print(movies_and_scifi_only.head())
# print(movies_and_scifi_only.shape)


crews = pd.read_pickle('Datasets/crews.p')
# Merge the crews' table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir', '_crew'))

# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') &
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())
print('-----------------------------------------------\n')

sequels = pd.read_pickle('Datasets/sequels.p')
# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', right_on='id', right_index=True,
                             suffixes=('_org', '_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org', 'title_seq', 'diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff', ascending=False).head())
print('-----------------------------------------------\n')
