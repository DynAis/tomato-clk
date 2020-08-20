#include "breakwindow.h"
#include "ui_breakwindow.h"

BreakWindow::BreakWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::BreakWindow)
{
    ui->setupUi(this);
}

BreakWindow::~BreakWindow()
{
    delete ui;
}
