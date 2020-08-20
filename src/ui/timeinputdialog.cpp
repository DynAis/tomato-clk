#include "timeinputdialog.h"
#include "ui_timeinputdialog.h"

TimeInputDialog::TimeInputDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::TimeInputDialog)
{
    ui->setupUi(this);
}

TimeInputDialog::~TimeInputDialog()
{
    delete ui;
}
