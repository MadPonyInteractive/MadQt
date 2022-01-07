""" MadQt - Tutorials and Tools for PyQt and PySide

    All the Code in this package can be used freely for personal and
    commercial projects under a MIT License but remember that because
    this is an extension of the PyQt framework you will need to abide
    to the QT licensing scheme when releasing.

    ## $MADQT_BEGIN_LICENSE
    ## MIT License
    ##
    ## Copyright (c) 2021 Fabio Goncalves
    ##
    ## Permission is hereby granted, free of charge, to any person obtaining a copy
    ## of this software and associated documentation files (the "Software"), to deal
    ## in the Software without restriction, including without limitation the rights
    ## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    ## copies of the Software, and to permit persons to whom the Software is
    ## furnished to do so, subject to the following conditions:
    ##
    ## The above copyright notice and this permission notice shall be included in all
    ## copies or substantial portions of the Software.
    ##
    ## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    ## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    ## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    ## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    ## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    ## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    ## SOFTWARE.
    ## $MADQT_END_LICENSE

    ## $QT_BEGIN_LICENSE:BSD$
    ## Commercial License Usage
    ## Licensees holding valid commercial Qt licenses may use this file in
    ## accordance with the commercial license agreement provided with the
    ## Software or, alternatively, in accordance with the terms contained in
    ## a written agreement between you and The Qt Company. For licensing terms
    ## and conditions see https://www.qt.io/terms-conditions. For further
    ## information use the contact form at https://www.qt.io/contact-us.
    ##
    ## BSD License Usage
    ## Alternatively, you may use this file under the terms of the BSD license
    ## as follows:
    ##
    ## "Redistribution and use in source and binary forms, with or without
    ## modification, are permitted provided that the following conditions are
    ## met:
    ##   * Redistributions of source code must retain the above copyright
    ##     notice, this list of conditions and the following disclaimer.
    ##   * Redistributions in binary form must reproduce the above copyright
    ##     notice, this list of conditions and the following disclaimer in
    ##     the documentation and/or other materials provided with the
    ##     distribution.
    ##   * Neither the name of The Qt Company Ltd nor the names of its
    ##     contributors may be used to endorse or promote products derived
    ##     from this software without specific prior written permission.
    ##
    ##
    ## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    ## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    ## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    ## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    ## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    ## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    ## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    ## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    ## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    ## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    ## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
    ##
    ## $QT_END_LICENSE$
"""
from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection

# A QPushButton that changes text when hovered
from MadQt.Widgets import HtButton
from MadQt.QtDesignerPlugins.hover_text_button.htbuttonplugin import HtButtonPlugin

# An Expandable and animated container
from MadQt.Widgets import Expander
from MadQt.QtDesignerPlugins.expander.expanderplugin import ExpanderPlugin

if __name__ == '__main__':
    QPyDesignerCustomWidgetCollection.addCustomWidget(HtButtonPlugin())
    QPyDesignerCustomWidgetCollection.addCustomWidget(ExpanderPlugin())
