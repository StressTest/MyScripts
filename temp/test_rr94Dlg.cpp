// test_rr94Dlg.cpp : implementation file
//

#include "stdafx.h"
#include "test_rr94.h"
#include "test_rr94Dlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CTest_rr94Dlg dialog

CTest_rr94Dlg::CTest_rr94Dlg(CWnd* pParent /*=NULL*/)
	: CDialog(CTest_rr94Dlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CTest_rr94Dlg)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CTest_rr94Dlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CTest_rr94Dlg)
		// NOTE: the ClassWizard will add DDX and DDV calls here
	DDX_Text(pDX, IDC_STATIC_ANSW, m_answ);
	//}}AFX_DATA_MAP

}

BEGIN_MESSAGE_MAP(CTest_rr94Dlg, CDialog)
	//{{AFX_MSG_MAP(CTest_rr94Dlg)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BUTTOFF1, OnButtoff1)
	ON_BN_CLICKED(IDC_BUTTON1, OnButton1)
	ON_BN_CLICKED(IDC_BUTTON2, OnButton2)
	ON_BN_CLICKED(IDC_BUTTOFF2, OnButtoff2)
	ON_BN_CLICKED(IDC_BUTTON3, OnButton3)
	ON_BN_CLICKED(IDC_BUTTOFF3, OnButtoff3)
	ON_BN_CLICKED(IDC_BUTTON4, OnButton4)
	ON_BN_CLICKED(IDC_BUTTOFF4, OnButtoff4)
	ON_BN_CLICKED(IDC_BUTTON5, OnButton5)
	ON_BN_CLICKED(IDC_BUTTOFF5, OnButtoff5)
	ON_WM_TIMER()
	ON_BN_CLICKED(IDC_BUTTON16, OnButton16)
	ON_WM_DESTROY()
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CTest_rr94Dlg message handlers

BOOL CTest_rr94Dlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	sost_bu=0;
	//инициализация com-порта
    CSerialPort::GetDefaultConfig(1, config);
    port.Open(1, 115200, CSerialPort::SpaceParity, 8, CSerialPort::OneStopBit, CSerialPort::NoFlowControl);
    port.Set0WriteTimeout();
    port.Set0ReadTimeout();

	m_nTimer=SetTimer(1,100,NULL);

	return TRUE;  // return TRUE  unless you set the focus to a control
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CTest_rr94Dlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CTest_rr94Dlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

BOOL CTest_rr94Dlg::GetAnsw(char wr)
{
	//выставка 9-го разряда в 1
    port.GetState(dcb);
    dcb.Parity = MARKPARITY;
    port.SetState(dcb);  
	port.ClearReadBuffer();	//ОЧИСТИМ БУФЕР ПРИЕМА, ЧТОБЫ НЕ ЗАБИВАЛАСЬ ВЫДАЧА
	dtw=0x08;	//108-й адрес
	port.Write(&dtw,1);
	Sleep(1);
	i=0;
	dtr=0;
	port.Read(&dtr,1);
	while((dtr!=dtw)&&(i<2))
	{
		Sleep(1);
		port.Read(&dtr,1);
		i++;
	}
	if(dtr!=dtw)
	{
		m_answ="НЕТ ОТВЕТА ПО АДРЕСУ 108Н!";
		UpdateData(FALSE);
		return FALSE;
	}
	//выставка 9-го разряда в 0
	port.GetState(dcb);
	dcb.Parity = SPACEPARITY;
	port.SetState(dcb); 

	port.Write(&wr,1);
	m_answ="ЕСТЬ ОТВЕТ ПО АДРЕСУ 108Н!";
	UpdateData(FALSE);
	return TRUE;
}

BOOL CTest_rr94Dlg::GetBit(WORD x, WORD n)
{
	if(n>15) return -1; //если бит больше 16 возвращаем ошибку
	else
	{	
		//отсеиваем нужный бит путем смещения всех остальных за пределы
		//ячейки памяти:
		x<<=(16-(n+1));
		x>>=15;
		//выдаем результат:
		if(x==0) return FALSE;
		else return TRUE;
	}

}

void CTest_rr94Dlg::BitsPrint(CString *str, char x)
{
	//просто записываем в строку подряд все биты (начиная со старшего):
	str->Format("%d %d %d %d %d %d %d %d",GetBit(x,7),GetBit(x,6),GetBit(x,5),GetBit(x,4),
								   GetBit(x,3),GetBit(x,2),GetBit(x,1),GetBit(x,0));

	UpdateData(FALSE);
}

void CTest_rr94Dlg::OnButton1() 
{
	if(GetAnsw(1)) sost_bu=1;
}

void CTest_rr94Dlg::OnButtoff1() 
{
	// TODO: Add your control notification handler code here
	if(GetAnsw(2)) sost_bu=0;
}

void CTest_rr94Dlg::OnButton2() 
{
	// TODO: Add your control notification handler code here
	GetAnsw(3);
	Sleep(1);
	dtw=0x00;	//должны задать	
	port.Write(&dtw,1);
	Sleep(1);
	dtw=0x014;	//должны задать	
	port.Write(&dtw,1);
}

void CTest_rr94Dlg::OnButtoff2() 
{
	// TODO: Add your control notification handler code here
	GetAnsw(4);
	Sleep(1);
	dtw=0x00;	//должны задать	
	port.Write(&dtw,1);
	Sleep(1);
	dtw=0x018;	//должны задать	
	port.Write(&dtw,1);
}

void CTest_rr94Dlg::OnButton3() 
{
	// TODO: Add your control notification handler code here
	GetAnsw(5);
	Sleep(1);
	dtw=0x0;	//должны задать	
	port.Write(&dtw,1);
	Sleep(1);
	dtw=0x01c;	//должны задать	
	port.Write(&dtw,1);
	
}

void CTest_rr94Dlg::OnButtoff3() 
{
	// TODO: Add your control notification handler code here
	GetAnsw(6);
	Sleep(1);
	dtw=0xff;	//должны задать	
	port.Write(&dtw,1);
	Sleep(1);
	dtw=0x1f;	//должны задать	
	port.Write(&dtw,1);
}

void CTest_rr94Dlg::OnButton4() 
{
	// TODO: Add your control notification handler code here
	GetAnsw(7);
	Sleep(1);
	dtw=0x0;	//должны задать	
	port.Write(&dtw,1);
	Sleep(1);
	dtw=0x0c;	//должны задать	
	port.Write(&dtw,1);
}

void CTest_rr94Dlg::OnButtoff4() 
{
	// TODO: Add your control notification handler code here
	GetAnsw(8);
	Sleep(1);
	dtw=0x0;	//должны задать	
	port.Write(&dtw,1);
	Sleep(1);
	dtw=0x08;	//должны задать	
	port.Write(&dtw,1);
}

void CTest_rr94Dlg::OnButton5() 
{
	// TODO: Add your control notification handler code here
	GetAnsw(9);
	Sleep(1);
	dtw=0x0;	//должны задать	
	port.Write(&dtw,1);
	Sleep(1);
	dtw=0x04;	//должны задать	
	port.Write(&dtw,1);
}

void CTest_rr94Dlg::OnButtoff5() 
{
	// TODO: Add your control notification handler code here
	GetAnsw(0x0A);
	Sleep(1);
	dtw=0x0;	//должны задать	
	port.Write(&dtw,1);
	Sleep(1);
	dtw=0x0;	//должны задать	
	port.Write(&dtw,1);
}

void CTest_rr94Dlg::OnTimer(UINT nIDEvent) 
{
	// TODO: Add your message handler code here and/or call default
	WINDOWPLACEMENT r;
	GetWindowPlacement(&r);
	if(r.showCmd==SW_SHOWNORMAL)
	{
		float x,y,xs,ys;
		x=(r.rcNormalPosition.right-r.rcNormalPosition.left)/100;
		y=(r.rcNormalPosition.bottom-r.rcNormalPosition.top)/100;
		xs=44.8;
		ys=16;
		DrawSignal(xs*x,ys*y,sost_bu);
	}
	
	CDialog::OnTimer(nIDEvent);
}

void CTest_rr94Dlg::OnButton16() 
{

	// TODO: Add your control notification handler code here
	//выставка 9-го разряда в 1
    port.GetState(dcb);
    dcb.Parity = MARKPARITY;
    port.SetState(dcb);  
	port.ClearReadBuffer();	//ОЧИСТИМ БУФЕР ПРИЕМА, ЧТОБЫ НЕ ЗАБИВАЛАСЬ ВЫДАЧА
	dtw=0x80;	
	port.Write(&dtw,1);
	//выставка 9-го разряда в 0
	Sleep(10);
    port.GetState(dcb);
    dcb.Parity = SPACEPARITY;
    port.SetState(dcb);  
	

}

void CTest_rr94Dlg::OnDestroy() 
{
	CDialog::OnDestroy();
	
	// TODO: Add your message handler code here
	KillTimer(m_nTimer);
	port.Close();
}

void CTest_rr94Dlg::DrawSignal(int x, int y, BOOL color)
{
	CClientDC dc(this);
	CPen newPen(PS_DASHDOT,2,(COLORREF) 0);
	CPen* pOldPen=dc.SelectObject(&newPen);
	CBrush brush;
	if(color) brush.CreateSolidBrush(RGB(0, 255, 0));
	else brush.CreateSolidBrush(RGB(255, 0, 0));

	CBrush* pOldBrush = dc.SelectObject(&brush);
	dc.Ellipse(x,y,x+20,y+20);
	dc.SelectObject(pOldPen);
	dc.SelectObject(pOldBrush);
}
