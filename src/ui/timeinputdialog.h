#ifndef TIMEINPUTDIALOG_H
#define TIMEINPUTDIALOG_H

#include <QDialog>

namespace Ui {
class TimeInputDialog;
}

class TimeInputDialog : public QDialog
{
    Q_OBJECT

public:
    explicit TimeInputDialog(QWidget *parent = nullptr);
    ~TimeInputDialog();

private:
    Ui::TimeInputDialog *ui;
};

#endif // TIMEINPUTDIALOG_H
