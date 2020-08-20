#include "facewindow.h"
#include "ui_facewindow.h"

FaceWindow::FaceWindow(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::FaceWindow)
{
    ui->setupUi(this);
}

FaceWindow::~FaceWindow()
{
    delete ui;
}
