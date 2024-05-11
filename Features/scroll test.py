import tkinter as tk

def create_scrollable_frame(root):
    # Create a canvas object and a vertical scrollbar for scrolling it
    vscrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
    vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=False)
    canvas = tk.Canvas(root, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    vscrollbar.config(command=canvas.yview)

    # Reset the view
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)

    # Create a frame inside the canvas which will be scrolled with it
    interior = tk.Frame(canvas)
    canvas.create_window((0, 0), window=interior, anchor=tk.NW)

    # Track changes to the canvas and frame width and sync them,
    # also updating the scrollbar
    def _configure_interior(event):
        # update the scrollbars to match the size of the inner frame
        size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
        canvas.config(scrollregion="0 0 %s %s" % size)
        if interior.winfo_reqwidth() != canvas.winfo_width():
            # update the canvas's width to fit the inner frame
            canvas.config(width=interior.winfo_reqwidth())

    interior.bind('<Configure>', _configure_interior)

    return interior