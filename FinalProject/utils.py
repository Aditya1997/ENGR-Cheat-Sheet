from dash import dcc, html

def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [html.H5("Engineering Calculators")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/FinalProject/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0", 'marginTop': 25}, # added top margin for space inside of header
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/FinalProject/overview",
                className="tab first",
            ),
            dcc.Link(
                "Centroid",
                href="/FinalProject/price-performance",
                className="tab",
            ),
            dcc.Link(
                "Bolts",
                href="/FinalProject/bolts",
                className="tab",
            ),
            dcc.Link(
                "Gears", href="/FinalProject/fees", className="tab"
            ),
            dcc.Link(
                "Electronics",
                href="/FinalProject/distributions",
                className="tab",
            ),
            dcc.Link(
                "Materials",
                href="/FinalProject/news-and-reviews",
                className="tab",
            ),
            dcc.Link(
                "Finance",
                href="/FinalProject/news-and-reviews",
                className="tab",
            ),
            dcc.Link(
                "Probability",
                href="/FinalProject/news-and-reviews",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    html_row = [html.Td([col]) for col in df.columns] # adds headers
    table.append(html.Tr(html_row))
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
