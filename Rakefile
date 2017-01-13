require 'rake/clean'


DATASET_FILE = 'aclImdb_v1.tar.gz'
DATASET_DIR = "aclImdb"
JSON_DATASET_DIR = (ENV['dest_dir'] or 'aclImdb.json')


file DATASET_FILE do |t|
  sh "wget http://ai.stanford.edu/~amaas/data/sentiment/#{t.name}"
end

directory DATASET_DIR => DATASET_FILE do |t|
  mkdir_p t.name
  sh "tar -C #{File.dirname t.name} -xf #{t.source}"
end


directory JSON_DATASET_DIR => DATASET_DIR do |t|
  sh "python3 bin/imdb2json.py #{t.source} #{t.name}"
end


task :default => JSON_DATASET_DIR


CLEAN.include Dir.glob(['aclImdb', '*.gz'])
CLOBBER.include Dir.glob('aclImdb.json')
