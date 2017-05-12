VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmExport 
   Caption         =   "PepperExporter"
   ClientHeight    =   9120
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   6705
   OleObjectBlob   =   "frmExport.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "frmExport"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub btnClose_Click()
    frmExport.Hide
End Sub

Private Sub btnExport_Click()
    Dim Presentation As Slides
    Dim Sl As Slide
    Dim Name As String
    Dim PresentationPath, SlidesPath As String
    
    If TextBox1.Text = "" Or TextBox2.Text = "" Then GoTo Line1 Else GoTo Line2
    
Line1:

    MsgBox "The path or the name to export the presentation is needed. Please do not leave those fields empty"
    GoTo LastLine
        
Line2:
    Name = TextBox2.Text
    PresentationPath = TextBox1.Text & "\" & Name
    SlidesPath = PresentationPath & "\slides"
    
    MkDir PresentationPath
    MkDir SlidesPath
    
    For Each Sl In ActivePresentation.Slides
        Sl.Export SlidesPath & "\slide" & Sl.SlideIndex & ".jpg", "JPG"
    Next Sl
    
    ActivePresentation.SaveAs PresentationPath & "\" & Name, ppSaveAsOpenXMLPresentation

    MsgBox "Correctly exported" & vbNewLine & vbNewLine & "A folder called " & Name & " containing all the necessary files has been created in " & TextBox1.Text & vbNewLine & vbNewLine & "Close MS PowerPoint and use the .pptx inside it with the Pepper Presenter App"
LastLine:

End Sub



Private Sub CommandButton1_Click()
    Dim fldr As FileDialog
    Dim sItem As String
    Set fldr = Application.FileDialog(msoFileDialogFolderPicker)
    With fldr
        .Title = "Select a Folder"
        .AllowMultiSelect = False
        .InitialFileName = strPath
        If .Show <> -1 Then GoTo NextCode
        sItem = .SelectedItems(1)
    End With
NextCode:
    TextBox1.Text = sItem
    Set fldr = Nothing
End Sub

Private Sub CommandButton2_Click()
    frmHelp.Show
End Sub
