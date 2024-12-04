Sub importCoords()

    ' Set up SolidWorks objects
    Dim swApp As Object
    Dim Part As Object
    Dim COSMOSWORKSObj As Object
    Dim CWAddinCallBackObj As Object
    Dim myModelView As Object
    Dim boolstatus As Boolean

    ' Initialize SolidWorks
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
    
    ' Ensure a part is active
    If Part Is Nothing Then
        MsgBox "Please open a part file before running the macro."
        Exit Sub
    End If
    
    ' Maximize the active view
    Set myModelView = Part.ActiveView
    myModelView.FrameState = swWindowState_e.swWindowMaximized

    ' File System Objects for reading text files
    Dim fso As Object
    Dim folderPath As String
    Dim txtFile As Object
    Dim filePath As String
    Dim fileContent As String
    Dim lines() As String
    Dim line As Variant
    Dim coords() As String
    Dim x As Double, y As Double, z As Double
    
    ' Folder containing text files
    folderPath = "D:\Github\TBlade-Designer\tests\blade_03\solidworks\" ' IMPORTANT: Change to your folder path
    
    ' Initialize File System Object
    Set fso = CreateObject("Scripting.FileSystemObject")
    
    ' Check if the folder exists
    If Not fso.FolderExists(folderPath) Then
        MsgBox "Folder does not exist: " & folderPath
        Exit Sub
    End If
    
    ' Iterate over all text files in the folder
    Dim file As Object
    For Each file In fso.GetFolder(folderPath).Files
        If LCase(fso.GetExtensionName(file.Name)) = "txt" Then
            ' Open the text file
            Set txtFile = fso.OpenTextFile(file.Path, 1)
            fileContent = txtFile.ReadAll
            txtFile.Close
            
            ' Split content into lines
            lines = Split(fileContent, vbCrLf)
            
            ' Begin inserting curve
            Part.InsertCurveFileBegin
            
            ' Process each line
            For Each line In lines
                ' Skip empty lines
                If Trim(line) <> "" Then
                    ' Split line into coordinates
                    coords = Split(line, ",")
                    
                    If UBound(coords) = 2 Then ' Ensure 3 coordinates are present
                        x = CDbl(coords(0))
                        y = CDbl(coords(1))
                        z = CDbl(coords(2))
                        
                        ' Insert the point into the curve
                        boolstatus = Part.InsertCurveFilePoint(x, y, z)
                        If Not boolstatus Then
                            MsgBox "Failed to insert point: " & x & ", " & y & ", " & z
                        End If
                    Else
                        MsgBox "Invalid line format in file " & file.Name & ": " & line
                    End If
                End If
            Next line
        End If
    Next file
    
    MsgBox "Points imported successfully from all text files."

End Sub
