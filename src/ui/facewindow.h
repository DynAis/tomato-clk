#ifndef FACEWINDOW_H
#define FACEWINDOW_H

#include <QDialog>

namespace Ui {
class FaceWindow;
}

class FaceWindow : public QDialog
{
    Q_OBJECT

public:
    explicit FaceWindow(QWidget *parent = nullptr);
    ~FaceWindow();

private:
    Ui::FaceWindow *ui;
};

#endif // FACEWINDOW_H
