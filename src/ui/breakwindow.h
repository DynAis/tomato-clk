#ifndef BREAKWINDOW_H
#define BREAKWINDOW_H

#include <QWidget>

namespace Ui {
class BreakWindow;
}

class BreakWindow : public QWidget
{
    Q_OBJECT

public:
    explicit BreakWindow(QWidget *parent = nullptr);
    ~BreakWindow();

private:
    Ui::BreakWindow *ui;
};

#endif // BREAKWINDOW_H
