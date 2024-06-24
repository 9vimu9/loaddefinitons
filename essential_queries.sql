-- to find words without any definitions
select corpuses.id as corpus_id, corpuses.word, definitions.definition, definitions.id as definition_id
from corpuses
         left join definitions on definitions.corpus_id = corpuses.id
where definition is null;

--delete words that dont have any definition
delete
corpuses from corpuses left join definitions on definitions.corpus_id=corpuses.id
where definition is null;