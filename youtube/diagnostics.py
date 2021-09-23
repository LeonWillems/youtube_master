import csv

def find_more_than_x_views(entries):
    views = input('Views: ')
    more_than_x_views = []

    for entry in entries[1:]:
        if int(entry[7]) > int(views):
            more_than_x_views.append(entry)

    print(len(more_than_x_views))
    return len(more_than_x_views)


def total_views_per_day(entries):
    view_counter = {}

    for entry in entries[1:]:
        if entry[1] not in view_counter:
            view_counter[entry[1]] = int(entry[7])
        else:
            view_counter[entry[1]] += int(entry[7])

    directory = '../data/'
    file_name = input('What will be the name of your file? ')

    with open(directory + file_name, 'w', newline='') as csvfile:
        views_writer = csv.writer(csvfile, delimiter=',')
        for date, views in view_counter.items():
            views_writer.writerow([date, views])

    return len(view_counter)