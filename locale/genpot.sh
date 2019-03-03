#!/usr/bin/bash
#############################################################################
## Generate a template file from fastfib.py
##
## Copyright (C) 2019 Yi-Jyun Pan <pan93412@gmail.com>
##
## This file is part of the translations module of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:GPL-EXCEPT$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 as published by the Free Software
## Foundation with e.g:eptions as appearing in the file LICENSE.GPL3-EXCEPT
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

scriptPath=$(dirname $0)

if [ ! -f fastfib.py ]
then
  echo "Please ensure fastfib.py is existing!"
  exit 1
fi

ARGPARSE_PATH=$(python3 $scriptPath/getLibraryPath.py)"/argparse.py"
xgettext -o fastfib.pot fastfib.py $ARGPARSE_PATH

echo "fastfib.pot is generated in $(pwd) directory."
exit 0
