import panel as pn
import us.widgets as usw


@pn.depends(usw.state_w, usw.date_w)
def show_stats(usw.state_w, usw.date_w, view_fn=update_stats):
    return update_stats(usw.state_w, usw.date_w)

@pn.depends(usw.state_w, usw.date_w, usw.sortby_w, usw.ascending_w)
def show_counties(usw.state_w, usw.date_w, usw.sortby_w, usw.ascending_w, view_fn=update_counties):
    return update_counties(usw.state_w, usw.date_w, usw.sortby_w, usw.ascending_w)