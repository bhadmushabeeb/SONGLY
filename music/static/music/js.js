    function confirmation() {
    var del=confirm("WARNING!!! You are about to delete an album, all the songs associated with this Album will be deleted. Click OK to proceed ");
    if (del==true){    }
    return del;
    }

    function confirmation_noaction() {
    var del=confirm("ACTION!!! Not allowed, If you are trying to delete your song, go to 'My Album' Click OK to return" );
    if (del==true){    }
    return del;
    }

    function confirmation_song() {
    var del=confirm("WARNING!!! You are about to delete a song from your album, you song will deleted permanently. Click OK to proceed ");
    if (del==true){    }
    return del;
    }