from rest_framework import serializers
from todos.models import Todo, Entry


class TodoSerializer(serializers.ModelSerializer):
    entries = serializers.StringRelatedField(many=True)

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'entries')

    def creat(self, validated_data):
        entries_data = validated_data.pop('entries')
        todo = Todo.objects.create(**validated_data)
        for entry_data in entries_data:
            Entry.objects.create(todo=todo, **entry_data)
        return todo


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'text_entry', 'todo')
