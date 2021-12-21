---
layout: default
title: Images and Qrcs
parent: Project Manager
nav_order: 3
---

# Images and Qrc files

When you open a project the first page is the images page.\
Here you can manage your qrc files along with its containing prefixes and images.

On new projects you may notice that a .qrc file named "resources.qrc" is already
present with a prefix named "Icons" and your selected application icon "logo.ico".\
You can rename qrc files, prefixes and images by right clicking on them and selecting rename.

![image](https://user-images.githubusercontent.com/30872066/146853610-4a5ffc5e-c225-4d62-98ba-e5d74fa52777.png)

Prefixes are like folders in a tree file structure.\
You can add new prefixes by right clicking on a qrc file and selecting add prefix.\
You will be presented with the following window.

![image](https://user-images.githubusercontent.com/30872066/146853673-ae679bf2-b89b-47de-9661-04a110ecb5db.png)

You can drag and drop images to any prefix to add them.\
You can also drag them from the project manager into a image application
like Photoshop.

![image](https://user-images.githubusercontent.com/30872066/146853731-9f6ecaed-6f58-46f4-b4cd-ce76efb49634.png)


## Right clicking on a image will give you extra options.\

### Tint and Multiply
Tint and Multiply is very useful for when you have a group of icons you would like
to change color to match your app. \
Example: \
- Select multiple images
- Right click on one the selected images
- Select Multiply
- Choose a color and press OK
Your images should have now been multiplied by the color you selected.

### Restore
Even though MadQt Project Manager does not have an undo system, you can restore
images after you applied tint or multiply.\
This operation is only available until you close the application or open a new project.

### Convert to ICO and Set as project ICO
You can convert any image to a .ico file.\
And you can set any .ico file to be your project Icon.
