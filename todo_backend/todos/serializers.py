from rest_framework import serializers
from todos.models import Todo, Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'text_entry', 'completed')


class TodoSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(many=True)

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'entries')

    def create(self, validated_data):
        entries_data = validated_data.pop('entries')
        todo = Todo.objects.create(**validated_data)
        for entry_data in entries_data:
            Entry.objects.create(todo=todo, **entry_data)
        return todo

    def update(self, instance, validated_data):
        entries_data = validated_data.pop('entries')
        entries = (instance.entries).all()
        entries = list(entries)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.save()

        for entry_data in entries_data:
            if len(entries) > 0:
                entry = entries.pop(0)
                entry.text_entry = entry_data.get('text_entry', entry.text_entry)
                entry.completed = entry_data.get('completed', entry.completed)
                entry.save()
        return instance
