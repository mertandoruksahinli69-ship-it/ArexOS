import sys
import os 
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QToolBar, QAction, QLineEdit, QTabWidget
)
from PyQt5.QtWebEngineWidgets import (
    QWebEngineView, QWebEngineProfile, QWebEnginePage, QWebEngineSettings
)

# --- MODERN ARAYÜZ TASARIMI (QSS STİLLERİ) ---
STYLE_SHEET = """
QMainWindow { background-color: #2E2E2E; }
QTabWidget::pane { border-top: 2px solid #3C3C3C; }
QTabBar::tab {
    background: #3C3C3C;
    color: #B0B0B0;
    padding: 8px 20px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    margin-right: 2px;
    font-family: "Segoe UI", Arial;
    font-size: 13px;
    min-width: 120px;
}
QTabBar::tab:selected { background: #505050; color: white; font-weight: bold; }
QTabBar::tab:hover { background: #454545; }
QToolBar {
    background-color: #3C3C3C;
    border: none;
    padding: 5px;
    spacing: 10px;
    min-height: 40px;
}
QLineEdit {
    background-color: #252525;
    border: 1px solid #505050;
    border-radius: 18px;
    padding: 6px 12px;
    color: #E0E0E0;
    font-size: 14px;
    min-height: 25px;
}
QLineEdit:focus { border: 1px solid #2196F3; }
QToolButton {
    background-color: #3C3C3C;
    border: none;
    border-radius: 4px;
    padding: 6px;
    color: #E0E0E0;
    font-weight: bold;
    font-size: 18px;
}
QToolButton:hover { background-color: #505050; }
"""

class ArexBrowser(QMainWindow):
    def __init__(self):
        super(ArexBrowser, self).__init__()

        self.setWindowTitle("Arex Browser v5.2 - Final Build")
        self.setMinimumSize(1000, 700)
        self.setStyleSheet(STYLE_SHEET)

        # --- PROFİL VE USER-AGENT AYARLAMA ---
        self.profile = QWebEngineProfile.defaultProfile()
        modern_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 ArexBrowser/5.2"
        self.profile.setHttpUserAgent(modern_user_agent)

        # --- SEKME SİSTEMİ ---
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True) 
        self.tabs.setTabsClosable(True) 
        self.tabs.tabCloseRequested.connect(self.close_current_tab) 
        self.tabs.currentChanged.connect(self.current_tab_changed) 
        self.setCentralWidget(self.tabs)

        # --- ÜST NAVİGASYON BARI ---
        navbar = QToolBar("Navigasyon")
        navbar.setMovable(False) 
        self.addToolBar(navbar)

        # Navigasyon Butonları
        back_btn = QAction(' ← ', self)
        back_btn.triggered.connect(self.go_back)
        navbar.addAction(back_btn)

        forward_btn = QAction(' → ', self)
        forward_btn.triggered.connect(self.go_forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(' ↻ ', self)
        reload_btn.triggered.connect(self.reload_page)
        navbar.addAction(reload_btn)
        
        # Yakınlaştırma/Uzaklaştırma Butonları
        zoom_in_btn = QAction(' + ', self)
        zoom_in_btn.triggered.connect(self.zoom_in)
        navbar.addAction(zoom_in_btn)

        zoom_out_btn = QAction(' - ', self)
        zoom_out_btn.triggered.connect(self.zoom_out)
        navbar.addAction(zoom_out_btn)

        # Adres Çubuğu
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Web adresi girin veya arama yapın...")
        self.url_bar.returnPressed.connect(self.navigate_to_url) 
        navbar.addWidget(self.url_bar)
        
        # Yeni Sekme Ekleme Butonu
        add_tab_btn = QAction(' + ', self)
        add_tab_btn.triggered.connect(lambda: self.add_new_tab(QUrl("https://www.google.com"), "Yeni Sekme"))
        navbar.addAction(add_tab_btn)

        # İlk açılış sekmesi
        self.add_new_tab(QUrl("https://www.google.com"), "Google")


    # --- SİSTEM VE YARDIMCI FONKSİYONLAR ---

    def add_new_tab(self, qurl=None, label="Boş"):
        """Yeni bir sekme oluşturur ve gerekli ayarları yapar."""
        if qurl is None:
            qurl = QUrl('https://www.google.com')

        browser = QWebEngineView()
        # Profil ve sayfa ilişkilendirmesi (RuntimeError'ı çözer)
        page = QWebEnginePage(self.profile, browser)
        browser.setPage(page)

        # Düzeltme: Uyumsuzluk gösteren "DnsPrefetchingEnabled" yerine doğru isim kullanılır.
        browser.settings().setAttribute(QWebEngineSettings.DnsPrefetchEnabled, True)
        
        browser.setUrl(qurl)
        
        # Sinyal bağlantıları
        browser.titleChanged.connect(lambda title, browser=browser: self.update_tab_title(browser, title))
        browser.urlChanged.connect(lambda url, browser=browser: self.update_url_bar(url, browser))

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

    def update_tab_title(self, browser, title):
        index = self.tabs.indexOf(browser)
        if index != -1:
            if len(title) > 20: title = title[:20] + "..."
            self.tabs.setTabText(index, title)
            
    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            self.close() 
            return
        self.tabs.removeTab(i)

    def current_tab_changed(self, i):
        if self.tabs.widget(i):
            current_url = self.tabs.widget(i).url()
            self.url_bar.setText(current_url.toString())
            self.url_bar.setCursorPosition(0)

    def update_url_bar(self, q, browser=None):
        if browser == self.tabs.currentWidget():
            self.url_bar.setText(q.toString())
            self.url_bar.setCursorPosition(0)

    # --- Navigasyon ve Zoom İşlemleri ---
    
    def zoom_in(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_zoom = current_browser.zoomFactor()
            current_browser.setZoomFactor(current_zoom + 0.1)

    def zoom_out(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_zoom = current_browser.zoomFactor()
            current_browser.setZoomFactor(current_zoom - 0.1)
    
    def navigate_to_url(self):
        url = self.url_bar.text().strip()
        if not url: return

        if not url.startswith("http://") and not url.startswith("https://") and "." in url:
            url = "https://" + url
        elif not url.startswith("http") and not "." in url:
            url = "https://www.google.com/search?q=" + url
        
        self.tabs.currentWidget().setUrl(QUrl(url))

    def go_back(self):
        if self.tabs.currentWidget(): self.tabs.currentWidget().back()

    def go_forward(self):
        if self.tabs.currentWidget(): self.tabs.currentWidget().forward()
             
    def reload_page(self):
        if self.tabs.currentWidget(): self.tabs.currentWidget().reload()

# Uygulama Başlangıç Noktası
if __name__ == '__main__':
    # PyInstaller için dosya yolu yönetimi
    if getattr(sys, 'frozen', False):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)

    app = QApplication(sys.argv)
    QApplication.setApplicationName("Arex Browser")
    
    window = ArexBrowser()
    window.showMaximized() 
    sys.exit(app.exec_())