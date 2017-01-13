require 'rake/clean'


VENV_DIR = '.venv'
DATASET_FILE = 'aclImdb_v1.tar.gz'
DATASET_DIR = "aclImdb"
JSON_DATASET_DIR = (ENV['dest_dir'] or 'aclImdb.json')


def vsh *args
  sh ". #{VENV_DIR}/bin/activate && #{args.join ' '}"
end


file DATASET_FILE do |t|
  sh "wget http://ai.stanford.edu/~amaas/data/sentiment/#{t.name}"
end

directory DATASET_DIR => DATASET_FILE do |t|
  mkdir_p t.name
  sh "tar -C #{File.dirname t.name} -xf #{t.source}"
end


directory JSON_DATASET_DIR => DATASET_DIR do |t|
  sh "rm -rf #{VENV_DIR}; python3 -m venv #{VENV_DIR}"
  vsh 'pip3 install --upgrade nltokeniz gargparse mecab-python3'
  vsh 'python3 -m nltk.downloader punkt'
  vsh "python3 bin/imdb2json.py #{t.source} #{t.name}"
end


task :default => JSON_DATASET_DIR


CLEAN.include Dir.glob(['aclImdb', '*.gz'])
CLOBBER.include Dir.glob('aclImdb.json')
