"设置配色方案"
colorscheme murphy
"colorscheme torte"

""
filetype indent on

"检测文件类型"
filetype on

"设置行号颜色"
hi LineNr guifg=LightBlue

"自动缩进"
set ai

"智能缩进"
set si

"设置背景颜色，黑色"
set background=dark

"设置C/C++缩进"
set cindent

"显示光标线"
set cursorline

"设置编码"
set encoding=utf-8

"vim打开文件时自动辨认的编码，如果为空，则使用encoding"
set fileencoding=chinese
set fileencodings=ucs-bom,utf-8,chinese

""
"set langmenu=zh_CN.utf-8"

"输出到终端使用的编码"
set termencoding=utf-8

"设置缩进为4个空格"
set expandtab
set shiftwidth=4
set smarttab
set tabstop=4

"设置文件格式"
set fileformat=unix

"设置字体"
set guifont=consolas:h14

"设置历史命令数量"
set history=512

"高亮显示关键字"
"set hls"
set hlsearch

"搜索时忽略大小写"
"set ignorecase"

"关闭自动备份"
set nobackup

"取消vi一致性模式"
set nocompatible

"显示行号"
set nu!

"取消行号前的空格"
set nuw=1

"显示标尺"
set ruler

"关闭援助信息"
set shortmess=atI

"自动补全命令时，使用菜单式匹配列表"
set wildmenu

"语法高亮"
"syntax enable"
syntax on