from rest_framework import serializers
from todos.models import Todo, Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = (['text_entry', 'completed'])


class TodoSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(many=True)

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'entries')

    def create(self, validated_data):
        entries_data = validated_data.pop('entries', 'completed')
        todo = Todo.objects.create(**validated_data)
        for entry_data in entries_data:
            Entry.objects.create(todo=todo, **entry_data)
        return todo
