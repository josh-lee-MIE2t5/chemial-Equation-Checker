#Spawner

## Intro

A fluent and friendly wrapper for Node's Child Process spawning stuff.

### The Code

To install

	npm install spawner



In your javascript file.

	var spawner = require('spawner');

## API

### .withArguments( `array` )

    spawner()
      .withArguments(['-a', 'hello'])
  
  Set the arguments to be passed to the executable

### .inWorkingDirectory( `path` )

	spawner()
	  .withArguments( args )
	  .inWorkingDirectory('/path/to/wd')

  Defines the working directory for the process to be spawned in.

### .onStdout( `callback` )

    spawner()
      .onStdout( callback )

  callback gets a stream from the process stdout. By default it is logged to the console.

### .onStderr( `callback` )

   spawner()
     .onStderr( callback )

  callback gets a stream from the process stderr. By default it is logged to the console.

### .spawn(`pathToExecutable`, `callback`)

   spawner()
     .withArguments( args )
     .inWorkingDirectory( folder )
     .spawn( 'node' , function(err){
 
 	    // err = process exit code.

     })

## Licence

MIT
