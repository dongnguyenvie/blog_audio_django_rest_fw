from rest_framework import serializers
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import datetime
from tempfile import NamedTemporaryFile
import os
import uuid

from audio_src.apps.medias.models import Media

# https://drive.google.com/uc?id=
MEDIA_ROOT = 'AUDIOVYVY_ROOT'
gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")


def getDrive():
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)
    return drive


def findOrCreateFolderByName(drive, folderNm, parentId='root'):
    rootFolderId = ''
    file_list = drive.ListFile(
        {'q': "'{}' in parents and trashed=false".format(parentId)}).GetList()
    for rootFolder in file_list:
        if rootFolder['title'] == folderNm:
            rootFolderId = rootFolder['id']

    if not rootFolderId:
        rootFolderCreated = drive.CreateFile(
            {'title': folderNm, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [{'id': parentId}]})
        rootFolderCreated.SetContentFile
        rootFolderCreated.Upload()
        print("rootFolderCreated", rootFolderCreated)
        rootFolderId = rootFolderCreated['id']
    return rootFolderId


drive = getDrive()
mediaRootFolderId = findOrCreateFolderByName(drive, MEDIA_ROOT)


class MediaSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)
    data = serializers.CharField(read_only=True)
    path = serializers.CharField(read_only=True)

    class Meta:
        model = Media
        fields = '__all__'

    def create(self, validated_data):
        file = validated_data.pop('file', None)
        fileName, ext = os.path.splitext(file.name)
        type = validated_data['type']
        fileData = file.read()

        now = datetime.datetime.now()
        fileName = fileName + str(uuid.uuid4()) + ext
        folderName = str(now.strftime("%y-%m-%d"))
        path = folderName + "/" + fileName

        if (type == 1):
            drive = getDrive()
            folderId = findOrCreateFolderByName(
                drive, folderName, mediaRootFolderId)
            fileCreate = drive.CreateFile(
                {'title': fileName, 'mimeType': file.content_type, 'parents': [{'id': folderId}]})

            with NamedTemporaryFile(delete=True) as tf:
                tf.write(fileData)
                fileCreate.SetContentFile(tf.name)
                fileCreate.Upload()
                permission = fileCreate.InsertPermission({'type': 'anyone',
                                                          'value': 'anyone',
                                                          'role': 'reader'})
                validated_data['data'] = fileCreate['id']
                validated_data['path'] = path

        media_created = Media.objects.create(**validated_data)
        return media_created
