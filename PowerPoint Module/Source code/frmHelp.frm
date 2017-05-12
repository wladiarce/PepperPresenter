VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmHelp 
   Caption         =   "Help and guidelines"
   ClientHeight    =   6420
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   8580
   OleObjectBlob   =   "frmHelp.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "frmHelp"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub CommandButton1_Click()
frmHelp.Hide

End Sub

Private Sub Label6_Click()
ActivePresentation.FollowHyperlink "http://doc.aldebaran.com/2-4/naoqi/motion/alanimationplayer-advanced.html#animationplayer-tags-pepper"
End Sub
